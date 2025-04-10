from flask import Blueprint, render_template, request
from datetime import datetime
import os

bp = Blueprint("chat", __name__)

def registrar_log(rota, mensagem):
    os.makedirs("logs", exist_ok=True)
    caminho = f"logs/{rota}.log"
    mensagem = mensagem.strip()
    if mensagem:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        origem = "USUÁRIO" if rota == "usuario" else "ATENDENTE"
        with open(caminho, "a") as f:
            f.write(f"[{timestamp}] [{origem}] {mensagem}\n")

def carregar_historico(rota):
    caminho = f"logs/{rota}.log"
    linhas_coloridas = []
    if os.path.exists(caminho):
        with open(caminho, "r") as f:
            linhas = list(reversed(f.readlines()))
            for linha in linhas:
                if "[USUÁRIO]" in linha:
                    cor = "red"
                elif "[ATENDENTE]" in linha:
                    cor = "blue"
                else:
                    cor = "black"
                linhas_coloridas.append(f'<font color="{cor}">{linha.strip()}</font>')
    return linhas_coloridas

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/usuario", methods=["GET", "POST"])
def usuario():
    if request.method == "POST":
        if "enviar" in request.form:
            msg = request.form["mensagem"]
            registrar_log("usuario", msg)
        elif "encerrar" in request.form:
            registrar_log("usuario", "CONVERSA ENCERRADA PELO USUÁRIO")
    historico = carregar_historico("usuario")
    return render_template("usuario.html", historico=historico)

@bp.route("/atendente", methods=["GET", "POST"])
def atendente():
    if request.method == "POST":
        if "enviar" in request.form:
            msg = request.form["mensagem"]
            registrar_log("atendente", msg)
        elif "encerrar" in request.form:
            registrar_log("atendente", "CONVERSA ENCERRADA PELO ATENDENTE")
    historico = carregar_historico("atendente")
    return render_template("atendente.html", historico=historico)
