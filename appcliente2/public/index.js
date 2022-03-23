async function readClientes() {
    const response = await axios.get('http://localhost:8000/clientes')

    const clientes = response.data

    const list = document.getElementById('lista-clientes')

    list.innerHTML = ''

    clientes.forEach(cliente => {
        const item = document.createElement('li')

        const info = `${cliente.nome} -> idade: ${cliente.idade} - sexo: ${cliente.sexo}`

        item.innerText = info

        list.appendChild(item)
    });

}

function sendClientes() {
    const form_cliente = document.getElementById('form-cliente')
    const input_nome = document.getElementById('nome')
    const input_idade = document.getElementById('idade')
    const input_sexo = document.getElementById('sexo')

    form_cliente.onsubmit = async(event) => {
        event.preventDefault()
        const nome_cliente = input_nome.value
        const idade_cliente = input_idade.value
        const sexo_cliente = input_sexo.value

        await axios.post('http://localhost:8000/clientes', {
            nome: nome_cliente,
            idade: idade_cliente,
            sexo: sexo_cliente
        })

        readClientes()
    }
}

function app() {
    console.log('App iniciado')
    readClientes()
    sendClientes()
}

app()