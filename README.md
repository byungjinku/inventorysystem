# inventorysystem

재고관리를 위한 입출고 시스템을 구성
쇼핑몰에서는 후드티와 청바지를 판매
후드티는 S, M, L,XL  양말, 모자 Free 사이즈가 있으며 청바지는 Free 사이즈를 판매

후드티의 종류는 총 3가지가 있으며 각각은 코드번호로 구분합니다. 
ex) hood-001, hood-002, hood-003 
청바지 코드는 다음과 같이 구분합니다. ex) jean-001 
재고는 수정이 가능해야하며 입,출고시 변화하는 수량을 반영할 수 있어야합니다. 


- 로그인, 로그아웃, 회원가입
    - Django 로그인 기능을 사용합니다.
```
Django에서 제공하는 로그인 기능을 사용할 경우 
Model을 작성하지 않고 form을 사용하는 것만으로도 로그인 기능을 만들 수 있습니다.
```
- 상품 등록
	
    - 코드번호와 상품의 종류 사이즈가 들어갑니다.

- 입고
    - 코드번호와 수량 입력으로 입고수량을 변화 시킬 수 있어야합니다.

- 출고
    - 코드번호와 수량 입력으로 출고수량을 변화 시킬 수 있어야합니다. 
    수량이 부족한 경우에는 출고를 할 수 없는 예외처리가 되어있어야 합니다.
    
- 화면구성
	
    - 로그인 페이지
    - 회원가입 페이지 
    - 재고관리 페이지
    
- 추가 요구사항
	
    - 현재 구성되어있는 Django 구조는 FBV를 기본으로 작성되어있을 거라고 생각합니다. 
    이 구조를 CBV로 변경해보세요 → FBV로 작성된 코드는 주석처리로 남겨두면 더 좋을 것 같습니다!
	
    - 입고/출고/검색 등의 재고와 관련된 부분을 form을 이용한 방식으로 재구성 해보세요
	
    - 상품을 추가하는 기능도 넣어보도록 하세요 
