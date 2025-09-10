## Redução de Dimensionalidade em Imagens para Redes Neurais.

![bairesDev](https://github.com/user-attachments/assets/f1bfd926-4bf3-4031-bab1-92aba768309e)


**Bootcamp BairesDev - Machine Learning Training**


---

**DESCRIÇÃO:**
Seguindo o exemplo do algoritmo de binarização apresentado em nossa última aula, realize a implementação em Python para transformar uma imagem colorida para níveis de cinza (0 a 255) e para binarizada (0 e 255), preto e branco.


---

<!-- badges: start -->
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Santosdevbjj/reduzImagensRedeNeural/ci.yml?branch=main)](https://github.com/Santosdevbjj/reduzImagensRedeNeural/actions)
[![Coverage](https://img.shields.io/codecov/c/github/Santosdevbjj/reduzImagensRedeNeural?branch=main)](https://codecov.io/gh/Santosdevbjj/reduzImagensRedeNeural)
[![License: MIT](https://img.shields.io/github/license/Santosdevbjj/reduzImagensRedeNeural)](https://opensource.org/licenses/MIT)
[![Last Commit](https://img.shields.io/github/last-commit/Santosdevbjj/reduzImagensRedeNeural)](https://github.com/Santosdevbjj/reduzImagensRedeNeural/commits/main)
<!-- badges: end -->

# Redução de Dimensionalidade em Imagens para Redes Neurais

Este projeto mostra como pré-processar imagens aplicando:
- **Tons de cinza** (0–255)
- **Binarização** (0 ou 255)

Um bom ponto de partida para aprendizado e redes neurais.

---

---

##  Estrutura do Projeto

<img width="1080" height="920" alt="Screenshot_20250910-184633" src="https://github.com/user-attachments/assets/93d93d50-f815-40df-aadc-9046a17731d8" />



---


**ci.yml:** configura CI com testes e cobertura.

**assets/:** imagens, incluindo a Lena original.

**src/:** scripts de conversão.

**demo.ipynb:** demonstração visual interativa.


---



**Como Rodar o Projeto**

**Instalação**

**git clone** https://github.com/Santosdevbjj/reduzImagensRedeNeural.git
cd reduzImagensRedeNeural
pip install -r requirements.txt

**Converter para Tons de Cinza**

python src/gray.py assets/lena_color.png assets/lena_gray.png

**Binarizar Imagem**

Com threshold fixo (padrão = 128):

python src/binary.py assets/lena_gray.png assets/lena_binary.png

**Com threshold adaptativo (Otsu):**

python src/binary.py assets/lena_gray.png assets/lena_binary_otsu.png



---

**Usando o Notebook**

**Execute o demo.ipynb localmente:**

**jupyter notebook demo.ipynb**

Ou abra com Google Colab. O notebook mostra:

1. Imagem colorida → grayscale → binarizada.


**2. Visualização lado a lado usando matplotlib.**




---

**Integração Contínua & Codecov**

Este projeto já está integrado com CI via GitHub Actions (.github/workflows/ci.yml):

Executa testes automatizados com pytest.

Gera relatórios de cobertura (coverage.xml) com pytest-cov.

Envia automaticamente os dados para o Codecov.

Badges mostram o status de build e cobertura diretamente no README.


**Para configurar o Codecov:**

1. Cadastre seu repositório em Codecov. Durante a configuração, copie o token de upload. 


2. No GitHub, vá em Settings → Secrets → Actions e crie um secret chamado CODECOV_TOKEN, colando o token capturado. 




---

**Tecnologias Utilizadas**

Python 3.x

NumPy, Pillow, scikit-image, Matplotlib

pytest, pytest-cov, codecov

GitHub Actions para CI



---

**Exemplo de Saídas**

Etapa	Arquivo Gerado

Tons de Cinza	assets/lena_gray.png
Binarização Fixa	assets/lena_binary.png
Binarização Otsu	assets/lena_binary_otsu.png



---

**Contribuições**

Contribuições são mais que bem-vindas!

1. Faça um fork do projeto.


2. Crie uma branch de feature:
git checkout -b feature-nome-da-feature


3. Faça suas modificações e commit.


4. Abra um Pull Request esperando até ser revisado.




---

**Licença**

Este projeto está sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.


---






