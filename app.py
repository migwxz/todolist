from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulação de banco de dados (lista de tarefas)
tasks = []

# Página inicial que lista as tarefas


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Adicionar uma nova tarefa


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']  # Pega o valor do campo de tarefa
    if task:  # Se a tarefa não estiver vazia
        tasks.append(task)  # Adiciona a tarefa à lista
    return redirect(url_for('index'))  # Redireciona para a página inicial

# Remover uma tarefa


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):  # Verifica se o ID da tarefa é válido
        tasks.pop(task_id)  # Remove a tarefa
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
