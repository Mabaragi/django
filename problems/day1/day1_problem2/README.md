# Django를 이용한 간단한 웹 계산기 구현

[계산기 입력으로 가기](project2\calculators\templates\calculators\calculation.html)

[계산기 출력으로 가기](project2\calculators\templates\calculators\catch.html)

[뷰 로직으로 가기](project2\calculators\views.py)

한 화면에 여러가지 입력 받기 가능. throw 함수에서 request 출력 하면 어떤 형식의 데이터인지 파악 가능함.

`request.GET` : 딕셔너리 형태
`request.GET.get()`으로 입력 데이터 가져가기.