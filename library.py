# legacy library system (simplified)

import datetime

def processa_emprestimo(usuario, livro):
    if usuario is None:
        return "Usuário inválido"

    if livro is None:
        return "Livro inválido"

    if not livro["disponivel"]:
        return "Livro indisponível"

    if usuario.get("bloqueado"):
        return "Usuário bloqueado"

    if "historico" not in usuario:
        usuario["historico"] = []

    hoje = datetime.datetime.now()
    data_devolucao = hoje + datetime.timedelta(days=7)

    livro["disponivel"] = False

    registro = {
        "livro": livro["titulo"],
        "data_emprestimo": hoje,
        "data_devolucao": data_devolucao
    }

    usuario["historico"].append(registro)

    return "OK"
