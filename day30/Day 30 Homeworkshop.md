# Day 30 Homeworkshop

## homework

1. JavaScript 는 ES6 이전과 이후로 많은 것이 바뀌었다 . ES5 까지는 ‘var’ 키워드로 변수를 선언했다면 , ES6 이후로는 ‘ 과 ‘const’ 키워드가 등장했다 . ‘ 과 ‘ 의 차이점과 언제 사용하는지에 대하여 간단하게 작성하시오.

  ```javascript
  let - 선언을 하고 재할당이 가능하다.
  const - constant 성질로 선언 후 재할당이 불가능하다.
  ```

  

2. JavaScript 에서는 Key Value 로 이루어진 자료 구조를 Object 라고 한다 . Object 와
   JSON 의 차이를 간단하게 작성하시오

   ```
   Object - 기본적으로 사용되는 데이터 형식
   JSON - 직렬화하여 JSON 형식의 string 값으로 변환한다.
   ```

   

3. 아래의 코드가 있을 때 value 에 접근하는 두 가지 방법을 코드로 작성하시오

![image-20191029171042739](../../../AppData/Roaming/Typora/typora-user-images/image-20191029171042739.png)

```javascript
myObject.key
```



## workshop


아래의 Python 코드를 JavaScript 코드로 다시 작성하시오
변수 및 함수 이름은 JavaScript naming convention( lowerCamelCase 을 따른다
Python 의 F String 은 JavaScript 의 Template Literal 을 사용한다

```javascript
const concat = function(str1, str2) {
  return str1 - str2
}

const check_long_str = function(string) {
  if (string.length > 10){
    return true
  }
  else {
    return false
  }
}

if (check_long_str(concat('Happy', 'Hacking')) === true){
  console.log('LONG STRING')
}
else {
  console.log('SHORT STRING')
}
```

