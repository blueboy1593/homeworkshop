# 12 workshop

## Problem

*스마트폰, 태블릿 PC, 노트북의 가로 해상도가 다음과 같을 때, 4개의 아이템이 각각의 기기에서 아래와 같이 보이도록 Bootstrap Responsive Grid System을 이용하여 구현하시오.*

```html
  <style>
    .item {
      background-color: salmon;
      border: 1px solid black;
      border-radius: 5px;
    }
  </style>

  <div class="container">
    <div class="row">
      <div class="item col-12 col-md-6 col-xl-3">1</div>
      <div class="item col-12 col-md-6 col-xl-3">2</div>
      <div class="item col-12 col-md-6 col-xl-3">3</div>
      <div class="item col-12 col-md-6 col-xl-3">4</div>
    </div>
  </div>
```

컨테이너로 row를 생성해 기본으로는 col-12, medium에서는 6, xl에서는 3으로 설정해주었다.

background 색상과 border는 워크샵과 맞춰주었다.
