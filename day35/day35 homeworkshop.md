# day35 homeworkshop

## homework

1. 빈칸 (a)에 들어갈 v-bind 디렉티브의 약어를 작성하시오. 

```
:
```

2. 빈칸 (a)에 들어갈 v-on 디렉티브의 약어를 작성하시오. 

```
@click
```

3.  Computed 속성과 watch 속성에 대하여 간단하게 설명하고, 이 둘의 차이점에 대해 작성하시오. 

 Vue는 Vue 인스턴스의 데이터 변경을 관찰하고 이에 반응하는 보다 일반적인 **watch 속성**을 제공합니다. 다른 데이터 기반으로 변경할 필요가 있는 데이터가 있는 경우, 특히 AngularJS를 사용하던 경우 `watch`를 남용하는 경우가 있습니다. 하지만 명령적인 `watch` 콜백보다 계산된 속성을 사용하는 것이 더 좋습니다.(역자 주: watch 속성은 감시할 데이터를 지정하고 그 데이터가 바뀌면  이런 함수를 실행하라는 방식으로 소프트웨어 공학에서 이야기하는 ‘명령형 프로그래밍’ 방식. computed 속성은 계산해야 하는  목표 데이터를 정의하는 방식으로 소프트웨어 공학에서 이야기하는 ‘선언형 프로그래밍’ 방식.) 

## workshop

 v-on 디렉티브를 활용하여, 다음과 같이 ‘+1’ 버튼을 누르면 숫자가 하나씩 증가하는 Counter 앱을 만들어 봅시다.  

```html
<div id="counter">
{{ count }}
<button v-on:click="plus">+1</button>
</div>
<script>
const app = new Vue({
      el: '#counter',
    
methods: {
    plus: function() {
        this.count++
    },
</script>
```

