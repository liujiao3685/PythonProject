import time, random

p_win = 0
e_win = 0

for count in range(1,4):
    print('第'+str(count)+'回合开始。。。。。。')
    # 生成双方角色，并生成随机属性。
    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    # 展示双方角色的属性
    print('【玩家】\n' + '血量：%s +  攻击：%s' %(player_life,player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
    print('------------------------')
    time.sleep(1)

    # 双方PK
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
        print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
        print('-----------------------')
        time.sleep(1.5)

    if player_life > enemy_life:
        p_win+=1
        print('你赢了')
    else:
        e_win+=1
        print('你输了')

if  p_win>e_win:
    print('三局连胜制你赢了')
elif  p_win<e_win:
    print('三局连胜制你赢了')
else:
    print('三局连胜制你输了')

# 打印战果
# 提示1:有三种结果，需要用到多向判断 if...elif...else
# 提示2:判断条件为双方的血量情况
