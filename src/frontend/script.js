document.addEventListener('DOMContentLoaded', function() {
    console.log('Frontend do Museu carregado!');
    
    // Carregar acervo dinamicamente do backend
    carregarAcervo();
    
    // Configurar formulário de contato
    const form = document.querySelector('#contato form');
    if(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = {
                nome: form.querySelector('input[type="text"]').value,
                email: form.querySelector('input[type="email"]').value,
                mensagem: form.querySelector('textarea').value
            };
            
            // Validação simples no frontend
            if (!formData.nome || formData.nome.length < 2) {
                alert('Nome deve ter pelo menos 2 caracteres');
                return;
            }
            if (!formData.email || !formData.email.includes('@')) {
                alert('Email inválido');
                return;
            }
            if (!formData.mensagem || formData.mensagem.length < 10) {
                alert('Mensagem deve ter pelo menos 10 caracteres');
                return;
            }
            
            fetch('/api/contato', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Mensagem enviada com sucesso!');
                    form.reset();
                } else {
                    alert(data.message || 'Erro ao enviar mensagem. Tente novamente.');
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Erro ao enviar mensagem. Tente novamente.');
            });
        });
    }
});

function carregarAcervo() {
    fetch('/api/acervo')
        .then(response => response.json())
        .then(data => {
            const acervoSection = document.getElementById('acervo');
            if (acervoSection && data.itens && data.itens.length > 0) {
                let html = '<h2>Acervo</h2><div class="acervo-grid">';
                data.itens.forEach(item => {
                    html += `
                        <div class="acervo-item">
                            ${item.imagem ? `<img src="/uploads/${item.imagem}" alt="${item.nome}" class="acervo-imagem">` : ''}
                            <div class="acervo-info">
                                <h3>${item.nome}</h3>
                                <p>${item.descricao || ''}</p>
                                ${item.categoria ? `<span class="categoria">${item.categoria}</span>` : ''}
                            </div>
                        </div>
                    `;
                });
                html += '</div>';
                acervoSection.innerHTML = html;
            } else {
                acervoSection.innerHTML = '<h2>Acervo</h2><p>Nenhum item encontrado no acervo.</p>';
            }
        })
        .catch(error => {
            console.error('Erro ao carregar acervo:', error);
            document.getElementById('acervo').innerHTML = '<h2>Acervo</h2><p>Erro ao carregar acervo.</p>';
        });
}
