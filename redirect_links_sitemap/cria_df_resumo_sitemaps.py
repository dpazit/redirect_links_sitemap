import os
import pandas as pd

def summarize_output_folder(output_folder):
    summary_data = []
    
    for filename in os.listdir(output_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(output_folder, filename)
            df = pd.read_csv(file_path, sep=',')
            
            # Conta quantos registros têm flag_redirect_errado como True
            qt_redirect_errado = df[df['flag_redirect_errado'] == True].shape[0]
            
            # Adiciona ao resumo
            summary_data.append((filename, qt_redirect_errado))
    
    # Cria o DataFrame final
    df_final = pd.DataFrame(summary_data, columns=['arquivo_destino', 'qt_redirect_errado'])
    
    return df_final

if __name__ == "__main__":
    output_folder = os.path.join(os.getcwd(), '../output')
    df_summary = summarize_output_folder(output_folder)
    
    # Exibindo o DataFrame final
    print("Resumo de redirecionamentos errados:")
    print(df_summary)
    
    # Exportando para um arquivo CSV
    output_csv_path = os.path.join(output_folder, 'resumo_sitemaps.csv')
    df_summary.to_csv(output_csv_path, index=False)
    
    print(f"Resumo exportado para: {output_csv_path}")
