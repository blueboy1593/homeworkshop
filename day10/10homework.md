# 10homework

## Problem1

```
1. CSS는 무엇의 약자인가? [ ]
(1) Creative Style Sheets
(2) Cascading Style Sheets
(3) Computer Style Sheets
(4) Colorful Style Sheets
```

답 : 2번 Cascading Style Sheets

## Problem2

```
다음 중 맞으면 T, 틀리면 F를 작성 하시오.
– HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. [T] 
– 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. [T] 
– 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다. [F]
```

## Problem3

```
크기 단위 em 은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?
```

rem.

루트의 단위를 가져오는 것이며, 여기서 루트란 제곱근이 아니라 HTML에서 최상단에 있는 세팅의 값이다.

## Problem4

```
다음 예제를 통해 ‘후손 셀렉터’와 '자식 셀렉터’의 차이를 설명하시오.
```

```css
/* 후손 셀렉터 */
div p {
  color: crimson;
}

/* 자식 셀렉터 */
div > p {
  color: crimson
}
```

자식 셀렉터는 직계 자식 하나에만 설정값이 적용이 된다.

후손 셀렉터는 하위에 속하는 모든 개체들에게 설정값 적용을 한다.

