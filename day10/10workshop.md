# 10 workshop

## Problem

*아래의 코드를 작성하여 몇 번째 단락이 빨간색으로 변하는지 확인해보자.*

```html
  <style>
    #ssafy > p:nth-child(2) {
      color: red;
    }
  </style>
  <div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
```

![style](C:\Users\student\development\homeworkshop\day10\style.JPG)

위의 코드로는 첫번째 단락에서 빨간 색상이 나타난다. 아마 child로 하면 위에 h2아래로 취급되어서 그런 것 같다.

p의 부모의 자식들 중에 두번째 아이가 p라면 적용시킨다는 뜻.

p가 두번째 아이가 아니면 아마도 적용이 안될 듯.

```html
  <style>
    #ssafy > p:nth-of-type(2) {
      color: blue;
    }
  </style>
```

![style2](C:\Users\student\development\homeworkshop\day10\style2.JPG)

위의 코드로는 두번째 단락에서 파란 색상이 나타난다. p라는 타입에서 2번째 항목이 선택되기에 처음 h2는 배제된다.

p:라는 것은 p인지를 물어보는 것과 같다.