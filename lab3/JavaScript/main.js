const input = document.getElementById('input');
const btn = document.getElementById('btn');
const list = document.getElementById('list');

let id = 0;

function addElement(toDo, id) {
    const text = `<li class="list__item">
                    <input type="checkbox" class="checkbox" id="${id}" job="complete">
                    <label class="label"> ${toDo}</label>
                    <span class="delete-icon" job="delete" id="${id}"></span>
                </li>`
    const position = 'beforeend'
    list.insertAdjacentHTML(position, text);
}

function completeToDo(element) {
    element.parentNode.querySelector('.label').classList.toggle('line');
}

function removeToDo(element) {
    element.parentNode.parentNode.removeChild(element.parentNode);
}


function pressBtn() {
    const toDo = input.value;
    if(toDo) {
        addElement(toDo, id);
        id++;
    }else {
        alert('Input is empty');
    }
    input.value = '';
}

list.addEventListener('click', function(event){
    let element = event.target;
    const elementJOB = event.target.attributes.job.value;
    if(elementJOB == 'complete') {
        completeToDo(element);
    }else if (elementJOB == 'delete') {
        removeToDo(element);
    }
});


