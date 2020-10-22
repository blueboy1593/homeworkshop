# Day 31 homeworkshop

## homework

1. DOM에서 특정 요소를 선택하 때, document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용할 수 있다. 이 둘의 차이를 간단하게 작성하시오.

```
document.querySelector()
특정 name 이나 id 를 제한하지않고 css선택자를 사용하여 요소를 찾습니다.

document.querySelectorAll()
querySelect 과 동일하게 작동하나 차이점은 해당 선택자에 해당하는 모든 요소를 가져옵니다.
반환객체는 nodeList이기때문에 for문 또는 foreach 문을 사용해야 합니다.
```



2. DOM에 요소를 추가할 때, ‘innerHTML += ...‘의 방법과 ‘apppendChild()’ 함수를 사용하는 방법이 있다. 이 둘의 차이를 간단하게 작성하시오.

appendChild는 현재 위치에 그냥 추가만 하는거고 
innerHTML은 전체태그에 합쳐지는 것
innerHTML += 를 사용해서계속적으로 전체데이터+추가데이터를 새로 쓰는 효과가 됩니다. 

appendChild는 추가데이터만 등록하는 효과. 추가 데이터만 필요할 때는 이것을 쓰면 됩니다. 훨씬 빠름



## workshop

