# day38 homeworkshop

## homework

 ❖ Axios는 다양한 HTTP 요청들을 브라우저나 Nodejs 환경에서 보낼 수 있는 JavaScript HTTP 클라이언트 라이브러리이다. 

1. CDN을 통하여 Axios를 사용하려 할 때, 어떠한 tag를 추가하여 해당 라이브러리를 불러와 사용할 수 있는지 작성하시오. 

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

2. NPM(Node Package Manager)을 통하여 Axios를 사용하려 할 때, Axios를 설치하는 명 령어는 무엇인지 작성하고, Vue 앱에서 어떻게 불러와 사용 할 수 있는지 작성하시오. 

```python
npm install axios
import axios from 'axios'
```

## workshop

 ❖ Axios를 활용하여, 아래 그림과 같이 ‘Get {N} Dogs!’ 버튼을 클릭하면 Dog API URL로 HTTP 요청을 보내어 임의의 강아지 사진을 지정한 개수만큼 가져와 보여주는 앱을 만 들어 봅시다. 

 ❖ 요청을 보낼 API URL은 입니다. 어떠한 형태로 데이터를 가져올 수 있는지 브라우저 주소창에 입력하여 확인해 보세요. 

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<div id="app">
<button v-on:click="getDogImage">드리는멍멍</button>
<img v-bind:src="dogImage" alt="멍멍">
</div>

<script>
methods: {
    getDogImage: function() {
        const API_URL = 'https://dog.ceo/api/breeds/image/random'
        axios.get(API_URL)
            .then((response) => {
            this.dogImage = response.data.message
        })
    },
</script>
```

