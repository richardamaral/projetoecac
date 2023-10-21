#  ❗📊 AUTOMAÇÃO PARA CONSULTA E RASPAGEM DE DADOS DO E-CAC PARA UMA PLANILHA 📊❗
![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Selenium Version](https://img.shields.io/badge/Selenium-3.141%2B-brightgreen)
![PyAutoGUI Version](https://img.shields.io/badge/PyAutoGUI-0.9%2B-brightgreen)
![Pandas Version](https://img.shields.io/badge/Pandas-2.1.1%2B-brightgreen)


Este projeto oferece uma solução automatizada para o processo de consultar e copiar as informações para uma planilha.
## Funcionalidades


- **CRIAÇÃO DAS LISTAS**: Ao iniciar o código, é definida algumas listas que serão preenchidas ao decorrer da execução do script, com a função .append para depois armazenar corretamente na planilha.

- **AUTENTICAÇÃO E-CAC**: Utilizando o (Selenium e PyAutoGUI), insiro um certificado digital no navegador para conseguir realizar consultas no E-CAC.

- **TÉCNICA DE ESPERA PROLONGADA**: Por conta do sistema do E-CAC ser bem inconsistente e fácil de dar erro nas páginas eu implementei um processo de espera fora do padrão para simular uma interação humana contínua e ocorrer menos erros de requisição ao servidor.

- **ITERAÇÃO TABELA XPATH**: Depois de chegar aonde me deparei com as 100 páginas de 20 empresas cada dentro do E-CAC, precisei estudar os endereços XPATH do site para assim conseguir criar uma iteração que correspondesse aos dados que eu queria realizar a raspagem de forma correta.

- **ENVIO PARA AS LISTAS**: De acordo com a execução das iterações presentes no código, é possível ver uma função ".append" nela que eu enviei os dados do loop para a lista para realizar a criação da planilha com a biblioteca Pandas depois.

  
 ****: Após o código ser executado é criada uma planilha com CNPJ/NOME/SITUACAO/DATA_VIGENCIA para facilitar a leitura e consulta e previsão de próximas expirações de outorga.

## Como Usar

1. **Configuração do Ambiente**:
   - Certifique-se de ter Python 3.8+ instalado.
   - Instale as bibliotecas necessárias com `pip install selenium pyautogui pandas`.
   - Insira um certificado digital na sua máquina, após isso execute o script com a resolução do monitor em 1440x900.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.

## Autor

- Richard Borges do Amaral
