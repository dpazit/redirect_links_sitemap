import os
import csv
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_redirect(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        final_url = response.url  # URL final após qualquer redirecionamento
        return final_url
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

def process_single_url(row, headers):
    original_url = row[0].strip()  # URL no arquivo
    redirected_url = fetch_redirect(original_url, headers)
    redirect_wrong_flag = (original_url != redirected_url)
    return (original_url, redirected_url, redirect_wrong_flag)

def process_csv_file_parallel(file_path):
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    filename = os.path.basename(file_path)
    print(f"Processando arquivo {filename} em paralelo...")
    
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        
        # Lista para armazenar as threads
        futures = []
        
        with ThreadPoolExecutor() as executor:
            # Processa cada linha do CSV em uma thread separada
            for index, row in enumerate(reader, start=1):
                if row:
                    future = executor.submit(process_single_url, row, headers)
                    futures.append(future)
            
            # Aguarda todas as threads completarem e coleta os resultados
            for future in as_completed(futures):
                results.append(future.result())
                print(f"Arquivo: {filename} - Link {len(results)} de {len(futures)}")

    print(f"Concluído o processamento do arquivo {filename}.")
    return results

def write_output_csv(results, output_folder, filename):
    output_file_path = os.path.join(output_folder, filename)
    
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['link_origem', 'link_destino', 'flag_redirect_errado'])
        
        for result in results:
            writer.writerow(result)

def start():
    input_folder = os.path.join(os.getcwd(), '../sitemap_urls')
    output_folder = os.path.join(os.getcwd(), '../output')
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            results = process_csv_file_parallel(file_path)
            output_filename = os.path.splitext(filename)[0] + '_output.csv'
            write_output_csv(results, output_folder, output_filename)
            print(f"Arquivo de output gerado: {output_filename}")

if __name__ == "__main__":
    start()
