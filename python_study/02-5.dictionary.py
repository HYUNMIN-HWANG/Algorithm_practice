#### dictionary : key-value

#### 추가, 삭제하기
a = {1 : 'a'}
a[2] = 'b'  # << {2: 'b'} 추가하기
print(a)    # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)    # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3]
print(a)    # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

del a[1]
print(a)    # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

del a['name']
print(a)    # {2: 'b', 3: [1, 2, 3]}


#### 딕셔너리 사용하기
# key를 사용해서 Value 를 얻을 수 있다.
dic = {'name':'pey', 'phone':'01012345678','birth':'0213'}
print(dic['name'])      # pey
print(dic['phone'])     # 01012345678
print(dic['birth'])     # 0213

#### 딕셔너리 주의사항
# 중복되는 key 값이 있으면 이전에 있던 key가 무시된다.
a = {1:'a', 1:'b'}
print(a)    # {1: 'b'}

# key에 리스트는 사용할 수 없다. 튜플은 쓸 수 있다.

#### 딕셔너리 관련 함수
# Keys
a = {'name':'pey', 'phone':'0101234','birth':'0212'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])
print(list(a.keys()))   # ['name', 'phone', 'birth']

# Values
print(a.values())   # dict_values(['pey', '0101234', '0212'])

# key : values
print(a.items())    # dict_items([('name', 'pey'), ('phone', '0101234'), ('birth', '0212')])

# 딕셔너리 모두 지우기
a.clear()
print(a)    # {}

# key로 value 얻기 
a = {'name':'pey', 'phone':'0101234','birth':'0212'}
print(a.get('name'))    # pey
print(a.get('phone'))   # 0101234
print(a.get('nokey'))   # Node >> 없는 key 값을 불러올 때 None을 반환해준다.
print(a.get('q','empty'))   # empty >> 없는 key 값을 불러올 경우, 디폴트로 지정한 empty를 가져온다.

# 해당 key가 딕셔너리 안에 있는지 조사하기
print('name' in a)  #True
print('puzzle' in a)    # False


