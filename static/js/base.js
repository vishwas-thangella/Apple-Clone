const bag = document.getElementById('shoppingBag');
const bar = document.getElementById('bar');

const HandleBar = () =>{
    if(bar.classList.contains('hidden')){
        bar.classList.remove('hidden');
    }else{
        bar.classList.add('hidden');
    }
}