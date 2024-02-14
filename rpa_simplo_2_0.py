import pyautogui as pa
import pyperclip as pc

pa.PAUSE = 0.3

pa.alert(text='Podemos iniciar a automação?', title='Início', button='SIM')

x, y = pa.locateCenterOnScreen('imagens/situacao.png')
pa.click(x=x, y=y)
x, y = pa.locateCenterOnScreen('imagens/situacao_exata.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
situacao = pc.paste().strip().capitalize()

x, y = pa.locateCenterOnScreen('imagens/cadastrais.png')
pa.click(x=x, y=y)

x, y = pa.locateCenterOnScreen('imagens/documento.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
documento = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/versao.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
versao = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/contrato.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
contrato = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/nome.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
nome = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/endereco.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
endereco = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/bairro.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
bairro = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/estado.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
estado = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/cep.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
cep = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/cidade.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
cidade = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/fixo.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
fixo = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/celular.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
celular = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/telefone_2.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
telefone_2 = pc.paste().strip()

x, y = pa.locateCenterOnScreen('imagens/seta.png')
pa.click(x=x, y=y-30)

x, y = pa.locateCenterOnScreen('imagens/email.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'c')
email = pc.paste().strip().lower()
if ';' in email:
    email = email.split(';')
elif ',' in email:
    email = email.split(',')

x, y = pa.locateCenterOnScreen('imagens/observacao.png')
pa.click(x=x, y=y+15)
pa.hotkey('ctrl', 'a')
pa.hotkey('ctrl', 'c')
observacao = pc.paste().strip()
quantidade_licencas = observacao.split(versao)
quantidade_licencas = str(quantidade_licencas[1]).split('*')

texto = f'''INFORMAÇÕES DO CLIENTE
{contrato} - {nome}
Situação: {situacao}
Versão: {versao}
Licenças: {quantidade_licencas[0]}

Documento: {documento}
Telefone Fixo: {fixo}
Celular: {celular}
Telefone: {telefone_2}
Email: {email}

Endereço: {endereco}, {bairro}, {cep} - {cidade}/{estado}

Histórico do Cliente:
    {observacao}
'''

pc.copy(texto)

pa.alert(text='Encerramos', title='Fim', button='OK')
