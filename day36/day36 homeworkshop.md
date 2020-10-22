# day36 homeworkshop

## homework

1.  아래와 같은 템플릿 코드와 Vue 인스턴스의 data 속성이 있을 때, 어떠한 HTML 코드가 렌더링 되는지 작성하시오. 

```
data의 active는 true로 'error' 는 false로
```

2.  아래와 같은 템플릿 코드와 Vue 인스턴스의 data 속성이 있을 때, 어떠한 HTML 코드가 렌더링 되는지 작성하시오. 

```
data 의 color 는 red 로, fontSize 는 30 으로 렌더링 된다.
```



## workshop

 v-bind 디렉티브의 class 또는 style 전달인자를 사용하여 아래와 같이 ‘Toggle’ 버튼을 클릭 할 때 마다 작성된 문장이 빨강과 파랑으로 변경되도록 하는 앱을 만들어 봅시다. 

```javascript
activeColor: 'red', 'blue'
methods: {
    toggleTodo: function(todo){
        todo.color = !todo.color
    },
```

