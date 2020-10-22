# day37 homeworkshop

## homework

1.  v-model 디렉티브는 input, textarea, select와 같은 엘리먼트들과 ____(a)____을 생성합 니다. 빈칸 (a)에 들어갈 말을 작성하시오.  

```
바인딩
```

2.  v-model 디렉티브는 엘리먼트의 종류에 따라 인스턴스의 속성을 업데이트하는 데이터 의 타입이 다릅니다. 아래의 엘리먼트들이 기본적으로 어떠한 데이터 타입으로 인스턴 스의 속성을 업데이트 하는지 https://kr.vuejs.org/v2/guide/forms.html를 참고하여 작 성하시오. 

 ▪ input ▪ textarea ▪ 단일 checkbox ▪ 다중 checkbox ▪ radio ▪ 단일 select ▪ 다중 select  



## workshop

 v-bind와 v-model 디렉티브를 활용하여, 다음과 같이 ‘Go!’ 링크를 누르면 입력 창에 작성한 URL로 이동 하도록 하는 ‘주소가 변하는 링크’를 만들어 봅시다. 

```html
<button v-on:click="gogoogle">Go!</button>
```

```javascript
methods: {
    gogoogle: function() {
        const URL = 'https://www.google.com'
        
        axios.get(URL)
            .then((response) => {
        })
    },
```

