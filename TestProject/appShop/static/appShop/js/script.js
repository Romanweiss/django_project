let addBucket = document.querySelectorAll('#addBucket')
addBucket.forEach((btn) => {
    btn.addEventListener('click', () => {
        let elements = btn.closest('.card')
        console.log(elements)
        let title = elements.querySelector('h1').textContent
        let productId = btn.getAttribute('data-product-id')

        let back = document.querySelector('.back')
        let content = document.createElement('div')
        content.innerHTML = `<p>${title}</p><button onclick="RBack(this)" id="removebacked" data-product-id="${productId}">Удалить</button>`
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

function RBack(event) {
    let productId = event.getAttribute('data-product-id');
    document.querySelector('.back').removeChild(event.closest('div'))
    $.ajax({
        type: 'POST',
        data: {
            id: productId,
            type:'remove',
            csrfmiddlewaretoken: document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
        }
    })
}


document.querySelector('#FormAjax').addEventListener('submit', (e)=>{
    e.preventDefault();
    let form = e.target
    console.log(form)
    let text = form.querySelector('textarea[name="desc"]').value
    let csrf_token = form.querySelector('input[name="csrfmiddlewaretoken"]').value
    $.ajax({
        type: "POST",
        url: form.getAttribute('action'),
        data: {
            csrfmiddlewaretoken: csrf_token,
            textarea: text,

        },
        success: function(response) {
            console.log(response)
        }
    })
})

// document.addEventListener('DOMContentLoaded', ()=>{
//     let bucket = document.querySelector('.bucket');
//     bucket.addEventListener('click', (e) => {
//         if (e.target && e.target.classList.contains('removebacked')) {
//             let btn = e.target;
//             console.log(btn);
//             btn.parentNode.remove(); // remove the parent node which is the div containing the product
//         }
//     });
// })

// $(document).ready(function () {
//     $('.addBucket').on('click', function () {
//         let elements = $(this).closest('.card');
//         let title = elements.find('h1').text();
//         let productId = $(this).data('product-id');

//         let bucket = $('.bucket');
//         let content = $('<div></div>').html(`<p>${title}</p><button class="removebacked" data-product-id="${productId}">Удалить</button>`);
//         bucket.append(content);

//         $.ajax({
//             type: 'POST',
//             data: {
//                 id: productId,
//                 csrfmiddlewaretoken: $('meta[name="csrf-token"]').attr('content'),
//             }
//         });
//     });

//     $('.bucket').on('click', '.removebacked', function () {
//         let btn = $(this);
//         console.log(btn);
//         btn.parent().remove(); // remove the parent node which is the div containing the product
//     });
// });

