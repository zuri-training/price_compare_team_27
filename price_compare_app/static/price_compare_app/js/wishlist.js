var updatebtns = document.getElementsByClassName('update-cart')

for (i =0; i < updatebtns.length; i++){
    updatebtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
         
        if (user === 'AnonymousUser'){
            console.log('User is not logged in')}else(
                updateUserOrder(productId, action)
            )    
     }
    )
}

function updateUserOrder(productId, action){
    var url = '/update_item/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        }, 
        body:JSON.stringify({
            'productId':productId,'action':action
        })
    })
    .then((response) => {return response.json()})
    .then((data) => {location.reload()})
}