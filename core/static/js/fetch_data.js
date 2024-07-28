function fetchData(input, urls) {
    const value = $.trim($(input).val());

    $.ajax({
        url: urls,
        type: 'GET',
        data: {'value': value},
        dataType: 'json',
        success: function (data) {
            console.log(data);
            document.getElementById('product-name').value = data.name;
        }
    });
}

// show and hide div based on selected items 
const dusElement = document.querySelectorAll('div.dus');
const bottleElement = document.querySelectorAll('div.bottle');
const rentengElement = document.querySelectorAll('div.renteng');

// hide all element in NodeList 
function hideElements(elements) {
    elements.forEach(element => {
        element.style.display = 'none'
    })
}

// show all element in a NodeList
function showElements(elements) {
    elements.forEach(element => {
        element.style.display = 'block'
    })
}

// set initial style for elements
hideElements(dusElement);
hideElements(bottleElement);
hideElements(rentengElement);

document.querySelector('select[name=product_type]').addEventListener('change', function() {
    if (this.value == 'renteng') {
        showElements(rentengElement);
        hideElements(bottleElement);
        hideElements(dusElement);
    }
    else if (this.value == 'dus') {
        showElements(dusElement);
        hideElements(bottleElement);
        hideElements(rentengElement);
    }
    else if (this.value == 'botol') {
        showElements(bottleElement);
        hideElements(dusElement);
        hideElements(rentengElement);
    }
});