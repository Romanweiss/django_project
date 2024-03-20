let addBucket = document.querySelectorAll('#addBucket')
addBucket.forEach((btn) => {
    btn.addEventListener('click', () => {
        let elements = btn.closest('.card')
        console.log(elements)
        let title = elements.querySelector('h1').textContent
        let productId = btn.getAttribute('data-product-id')

        let bucket = document.querySelector('.bucket')
        let content = document.createElement('div')
        content.innerHTML = `<p>${title}</p><button data-product-id="${productId}">Удалить</button>`
        bucket.appendChild(content)

        $.ajax({
            type: 'POST',
            data: {
                id: productId,
                csrfmiddlewaretoken: document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
            }
        })

    })
})