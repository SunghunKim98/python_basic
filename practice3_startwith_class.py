# Class

# 마린: 공격 유닛, 군인, 총을 쏠 수 있음


# __init__ 이라는 것은 "생성자"

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        # 위의 내용처럼 상속을 받아서 사용가능
        # self.name = name
        # self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")
        else:
            print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

# 날 수 있는 기능을 가진 클래스

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# 공중 공격 유닛 클래스 -> "다중 상속"
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)





