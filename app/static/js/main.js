$(document).ready(main);
var contador = 1;
function main() {
    $(".menubar").click(function () {
        if (contador == 1) {
            $('nav').animate({
                left: '0'
            })
            contador = 0;
        } else {
            contador = 1;
            $('nav').animate({
                left: '-100%'
            });
        }
    });
    // mostramos y oculatamos submenus

    $('.submenu').click(function () {
        $(this).children('.children').slideToggle();
    });
}
const getTitleMessageFromCategory = category => {
    const titles = {
        'success': 'Bien Hecho',
        'warning': 'Atencion',
        'info': 'Atencion',
        'error': 'Oops...!',

    }
    return titles[category]
}

function showMessageAlert(category, message) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })

    Toast.fire({
        icon: category,
        title: getTitleMessageFromCategory(category),
        text: message
    })
}






