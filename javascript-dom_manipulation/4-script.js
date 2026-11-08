#!/usr/bin/node
const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function () {
  const list = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
