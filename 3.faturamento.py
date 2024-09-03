import json
import xml.etree.ElementTree as ET

def ler_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def ler_xml(caminho_arquivo):
    try:
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
        
        dados_xml = []
        for row in root.findall('row'):
            dia = int(row.find('dia').text)
            valor = float(row.find('valor').text)
            dados_xml.append({"dia": dia, "valor": valor})
        
        return dados_xml
    except ET.ParseError as e:
        print(f"Erro ao parsear o XML: {e}")
        return []

def calcular_estatisticas(dados):
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    if not valores:
        print("Nenhum valor disponível para calcular as estatísticas.")
        return

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
    
    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

caminho_json = r'C:\Users\lucas\OneDrive\Área de Trabalho\3.faturamento\dados.json'
caminho_xml = r'C:\Users\lucas\OneDrive\Área de Trabalho\3.faturamento\dados (2).xml'

dados_json = ler_json(caminho_json)
dados_xml = ler_xml(caminho_xml)

print("Estatísticas para o JSON:")
calcular_estatisticas(dados_json)

print("\nEstatísticas para o XML:")
calcular_estatisticas(dados_xml)

# Como enviaram os arquivos de apoio depois da minha primeira resolutiva, adaptei ambos(json e xml) no exercício 3.
