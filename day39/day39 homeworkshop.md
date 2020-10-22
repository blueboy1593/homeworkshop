# day39 homeworkshop

## homework

1. 아래 그림과 같이 새로운 글을 작성하기 위해 Axios를 사용하여 ‘/articles/create/’로 POST 요청을 보내려 할 때, 아래의 빈칸 (a), (b)에 들어갈 코드를 작성하시오.

```
a) get
b) ‘/articles/create/’
```

2. CORS가 무엇의 약자인지 작성하고, 의미하는 바가 무엇인지 간단하게 작성하시오. 

CORS(Cross-Origin Resource Sharing)

 CORS(Cross-origin 리소스 공유)는 한 도메인에서 로드되어 다른 도메인에 있는 리소스와 상호 작용하는 클라이언트 웹 애플리케이션에 대한 방법을 정의합니다.

## workshop

 ❖ Axios를 활용하여, 아래 그림과 같이 ‘Get Posts’ 버튼을 클릭하면 특정 URL로 HTTP 요청을 보내어 임의의 Post의 리스트를 가져와 보여주는 앱을 만들어 봅시다.

 ❖ 요청을 보낼 URL은 입니 다. 어떠한 데이터들을 가져올 수 있는지 브라우저 주소창에 입력하여 확인해 보세요. 

```html
<script>
import axios from 'axios'
const URL = 'https://jsonplaceholder.typicode.com/posts'
export default {
    methods: {
		axios.get(API_URL)        
    }
</script>
```

