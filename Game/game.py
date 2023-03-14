# This implements a game engine designed by UVA all credit for it is given with the uvage.py project file

# The character has basic mobility, with walking and jumping. He is also able to attack as well. This will be used in
# order to defeat the enemy. The enemy is able to attack the player and depleted his hearts, once all four are gone then
# it is game over. The enemy's attacks have a bit of start up and end time that allow the player to attack. Jumping over
# the enemy is also a strategy to be used in order to get a hit in. The enemy will start of with a base attack speed,
# walk speed, and health amount. But these numbers get greater everytime the enemy is defeat. He will respawn again with
# greater power. The objective of the game is to see how many waves the player can get to, this correlates with a score.

# The tactic to defeating the enemy is to either time an attack from the front when being approached or to jump behind
# the enemy while he is attacking and attack. When the enemy's movement and attack gets fast enough, attacking from the
# front will not work nor will regularly jumping around to attack. This is when the quick fall action will help as it
# causes the player to fall faster, making it easier to hit the enemy from behind when it is in attack time.

# User Input: Left-Right Movement with "arrow keys" or "a" and "d", Jumping with "up arrow" or "w", attack with
# "space", quick fall with "down arrow" or "s"

# Game Over: Once all 4 hearts deplete, Game Over screen pops up and all movement is ceased
# Graphics/Images: This is used through the background, HUD, character, enemy, and game over screen

# Restart from Game Over: When game over occurs, press "r" or "space" to restart
# Sprite Animation: These are include in all action the character takes as well as the enemy
# Enemies: The enemies come as one, who gets progressively stronger as the rounds go by
# Health Bar: Four hearts displayed at the top-left, if the character takes damage from enemy attack, a heart is lost

# Hit Boxes: There are 4 types of hit boxes that are made invisible once the game starts: The character, the enemy, the
# character's attack, and the enemy's attack. When attack overlaps with the opposing person, they are knocked back

import uvage as uvage
import random

# Global Numbers
screen_width = 1000
screen_height = 600
camera = uvage.Camera(screen_width, screen_height)
walk_speed = 7
enemy_walk_speed = 2
score = 0  # This will be the amount of enemies defeated
frame = 0  # This is used for the walking animation
frame2 = 0  # This is used for the attack animation
frame3 = 0  # This is used for the enemy walking animation
frame4 = 0  # This is used for the enemy attack animation
end_time_lag = 0  # This is frames for how long it takes for the enemy to move/attack again
knockback_count = 0  # This is how many frames the character is knocked back for
knockback_count2 = 0  # This is how many frames the enemy is knocked back for
spawn_time = 0  # This is how many frames until respawn time
hit_counts = 0  # This will be how many times the enemy has been hit
enemy_health = 1  # This is the amounts of hits it takes to beat the enemy
attack_frames = 12  # This is the total frames the enemy's attack takes
lag_count = 0  # Counts for lag to be over
lag = 0  # State in which attack is in lag time

# Global Conditionals
facing_right = True  # Used for walking function
facing_right2 = True  # Used for enemy
in_air = False  # State that character is in the air
in_air2 = False  # State that enemy is in the air
attacking = False  # State that the character is currently attacking
enemy_attacking = False  # State that the enemy is currently attacking
hit = False  # State that the character is currently hit
hit2 = False  # State that the enemy is currently hit
heart_loss = False  # State that a heart was just lost
gameover = False  # State that the game has just ended
respawn = False  # State that the enemy can respawn

# Environment Details
background = uvage.from_image(screen_width // 2, screen_height // 2, "WideScreenBackground.png")
floor = uvage.from_color(screen_width/2, screen_height + 221, "blue", screen_width, screen_height)
walls = [
    uvage.from_color(-500, screen_height/2, "black", screen_width, screen_height),
    uvage.from_color(1500, screen_height/2, "black", screen_width, screen_height)
]
gameover_screen = uvage.from_image(screen_width // 2, screen_height // 2, "Gameover.png")

# Hit Boxes
hitbox = uvage.from_color(-500, 444, "blue", 70, 140)  # Character attack
hitbox2 = uvage.from_color(-500, 460, "yellow", 120, 70)  # Enemy Attack
character_hitbox = uvage.from_color(0, 0, "green", 100, 140)  # Character hit box
enemy_hitbox = uvage.from_color(0, 0, "red", 120, 140)  # Enemy hit box


# Character Details
character_idle = uvage.load_sprite_sheet("GarfieldIdle.png", rows=1, columns=1)
character_walk = uvage.load_sprite_sheet("GarfieldWalk.png", rows=1, columns=10)
character_jump = uvage.load_sprite_sheet("GarfieldJump.png", rows=1, columns=11)
character_attack = uvage.load_sprite_sheet("GarfieldAttack.png", rows=1, columns=5)
character_hurt = uvage.load_sprite_sheet("GarfieldHurt.png", rows=1, columns=4)
character_hud = uvage.from_image(70, 70, "GarfieldHUD.png")

character = uvage.from_image(500, 600, character_idle[-1])
character.size = (140, 140)

# Enemy Details
enemy_idle = uvage.load_sprite_sheet("OdieIdle.png", rows=1, columns=1)
enemy_walk = uvage.load_sprite_sheet("OdieWalk.png", rows=1, columns=7)
enemy_attack = uvage.load_sprite_sheet("OdieAttack.png", rows=1, columns=4)
enemy_hurt = uvage.load_sprite_sheet("OdieHurt.png", rows=1, columns=3)

enemy = uvage.from_image(700, 400, enemy_idle[-1])
enemy.size = (280, 140)

# Health Files
life4 = uvage.from_image(130, 70, "HeartFull.png")
life3 = uvage.from_image(165, 70, "HeartFull.png")
life2 = uvage.from_image(200, 70, "HeartFull.png")
life1 = uvage.from_image(235, 70, "HeartFull.png")
life = {life1: True, life2: True, life3: True, life4: True}


def create():
    """
    This creates the barriers of the stage. Cannot walk off, creates ground and background
    :return:
    """
    camera.draw(floor)
    camera.draw(character_hitbox)
    camera.draw(enemy_hitbox)
    camera.draw(hitbox)
    camera.draw(hitbox2)
    camera.draw(background)
    for wall in walls:
        camera.draw(wall)


def walking():
    """
    The walking controls are made here along with the animations
    :return:
    """
    global character, walk_speed, frame, facing_right, walls, hit
    moving = False
    # Moving Left or Right
    if uvage.is_pressing("right arrow") or uvage.is_pressing("d") and not (attacking or hit):
        character.x += walk_speed
        moving = True
        if not facing_right:
            character.flip()
            facing_right = True
    if uvage.is_pressing("left arrow") or uvage.is_pressing("a") and not (attacking or hit):
        character.x -= walk_speed
        moving = True
        if facing_right:
            character.flip()
            facing_right = False
    # Walking Animation
    if not moving:
        character.image = character_idle[0]
    else:
        frame += .2
        if frame >= 10:
            frame = 0
        character.image = character_walk[int(frame)]
    # Wall Collision
    for wall in walls:
        character.move_to_stop_overlapping(wall)
    # Hurt Animation
    if hit:
        character.image = character_hurt[int(knockback_count/8)]


def jumping():
    """
    The jumping and quick fall controls are made here along with the animations
    :return:
    """
    global character, camera, floor, character_jump, in_air, frame2
    # Gravity
    character.speedy += 1
    # Jumping
    if character.bottom_touches(floor):
        character.move_to_stop_overlapping(floor)
        character.speedy = 0
        in_air = False
        if uvage.is_pressing("up arrow") or uvage.is_pressing("w") and not (attacking or hit):
            character.speedy = - 25
            in_air = True
    # Jumping Animation
    if in_air:
        if character.speedy < 0:
            character.image = character_jump[int((character.speedy + 17)/5)]
        elif character.speedy == 0:
            character.image = character_jump[4]
        elif character.speedy > 0:
            character.image = character_jump[int((character.speedy + 17) / 5)]
    if character_hitbox.touches(hitbox2):
        character.yspeed = -4
    character.move_speed()
    # Quick Fall
    if in_air:
        if uvage.is_pressing("down arrow") or uvage.is_pressing("s") and not (attacking or hit):
            character.speedy += 1


def attack():
    """
    The attacking controls are made here along with animations
    :return:
    """
    global frame2, attacking, hitbox, character, facing_right, lag, lag_count
    # Attack Key
    if uvage.is_pressing("space") and not hit and not lag:
        attacking = True
    # Attack State
    if attacking:
        hitbox.y = character.y
        if facing_right:
            hitbox.x = character.x + 40
        else:
            hitbox.x = character.x - 40
        frame2 += 0.15
        character.image = character_attack[int(frame2)]
        if int(frame2) == 0 or int(frame2) == 3 or int(frame2) == 5:
            hitbox.x = -500
        if frame2 > 4:
            frame2 = 0
            lag = True
            attacking = False
    else:
        hitbox.x = -500
    # End Lag
    if lag:
        lag_count += 1
    if lag_count == 24:
        lag_count = 0
        lag = False



def knockback():
    """
    This is responsible for the pushback when the player or enemy is attacked
    :return:
    """
    global character, enemy, character_hitbox, enemy_hitbox, hitbox, hitbox2, facing_right, facing_right2, hit, hit2, \
        knockback_count, knockback_count2, heart_loss, character_hurt, hit_counts
    # When character is hit
    if character_hitbox.touches(hitbox2):
        hit = True
    if hit and not facing_right2:
        character.speedx = -8
        knockback_count += 1
        if knockback_count > 30:
            character.speedx = 0
            knockback_count = 0
            hit = False
            heart_loss = True
    if hit and facing_right2:
        character.speedx = 8
        knockback_count += 1
        if knockback_count > 30:
            character.speedx = 0
            knockback_count = 0
            hit = False
            heart_loss = True
    # When enemy is hit
    if enemy_hitbox.touches(hitbox):
        hit2 = True
    if hit2 and not facing_right:
        enemy.speedx = -8
        knockback_count2 += 1
        if knockback_count2 > 20:
            enemy.speedx = 0
            knockback_count2 = 0
            hit2 = False
            hit_counts += 1
    if hit2 and facing_right:
        enemy.speedx = 8
        knockback_count2 += 1
        if knockback_count2 > 20:
            enemy.speedx = 0
            knockback_count2 = 0
            hit2 = False
            hit_counts += 1


def health():
    """
    This is responsible for depleting a heart when attacked
    :return:
    """
    global character_hud, life, heart_loss
    camera.draw(character_hud)
    for heart in life:
        camera.draw(heart)
        if heart_loss and life[heart]:
            heart.image = "HeartEmpty.png"
            heart_loss = False
            life[heart] = False


# def recover():
    # This will recover a heart, either through an item drop or by not getting hit for a while


def enemies():
    """
    This gives all functions to the enemy: Gravity, Movement, Attack
    :return:
    """
    global enemy, character, facing_right2, frame3, enemy_attacking, frame4, hitbox2, end_time_lag, enemy_walk_speed, \
        in_air2, attack_frames
    # Gravity
    enemy.speedy += 0.5
    if enemy.speedy > 0:
        in_air2 = True
    if enemy.touches(floor):
        enemy.move_to_stop_overlapping(floor)
        enemy.speedy = 0
        in_air2 = False
    enemy.move_speed()
    # Movement
    moving = False
    if enemy_attacking or hit2:
        moving = False
    elif character.x + 80 < enemy.x and not in_air2:
        enemy.x -= enemy_walk_speed
        moving = True                        
        if facing_right2:                    
            enemy.flip()                     
            facing_right2 = False            
    elif character.x - 80 > enemy.x and not in_air2:
        enemy.x += enemy_walk_speed
        moving = True                        
        if not facing_right2:                
            enemy.flip()                     
            facing_right2 = True
    for wall in walls:
        enemy.move_to_stop_overlapping(wall)
    # Movement Animation                     
    if not moving:                           
        enemy.image = enemy_idle[0]          
    else:                                    
        frame3 += .2                         
        if frame3 >= 7:                      
            frame3 = 0                       
        enemy.image = enemy_walk[int(frame3)]
    # Attack
    if not moving:
        if enemy.x <= character.x + 80:
            if facing_right2:
                hitbox2.x = enemy.x + 70
            elif not facing_right2:
                hitbox2.x = enemy.x - 70
            enemy_attacking = True
    # Attack Animation
    if enemy_attacking:
        end_time_lag += 0.2
        frame4 += 0.2
        if (attack_frames/4) < end_time_lag < ((attack_frames * 3)/4):
            enemy.image = enemy_attack[int(frame4)]
        if end_time_lag > ((attack_frames * 3)/4) or end_time_lag < (attack_frames/4):
            hitbox2.x = -500
        if frame4 > 3:
            frame4 = 0
        if end_time_lag > attack_frames:
            enemy_attacking = False
            end_time_lag = 0
    else:
        hitbox2.x = -500
    # Hit
    if hit2:
        enemy.image = enemy_hurt[int(knockback_count2/7)]


def hitboxes():
    """
    This functions tracks where the character and enemy hit boxes are placed
    :return:
    """
    global character, enemy, character_hitbox, enemy_hitbox
    character_hitbox.x = character.x
    character_hitbox.y = character.y
    enemy_hitbox.x = enemy.x
    enemy_hitbox.y = enemy.y


def defeated():
    """
    This function manages what happens when the enemy is defeat, such as respawn and incresed difficulty
    :return:
    """
    global hit_counts, enemy_health, score, spawn_time, respawn, enemy_walk_speed, attack_frames
    # Killed
    if hit_counts == enemy_health:
        score += 1
        enemy.x = 1500
        respawn = True
        hit_counts = 0
    # Respawn
    if respawn:
        spawn_time += 1
        if spawn_time == 120:
            enemy.x = random.randrange(300, 700)
            enemy.y = 0
            enemy_walk_speed += 1
            if (enemy_walk_speed % 2) == 0:
                enemy_health += 1
            if attack_frames != 1:
                attack_frames -= 0.5
            respawn = False
            spawn_time = 0


def game_over():
    """
    This causes for the game to end as well as restart
    :return:
    """
    global life, gameover, life4, life3, life2, life1, score, enemy_walk_speed, enemy_health, hit_counts, attack_frames
    if not life[life4]:
        camera.draw(gameover_screen)
        gameover = True
    if uvage.is_pressing("r") or uvage.is_pressing("space") and gameover:
        # Character Reset
        character.x = 500
        character.y = 600
        hit_counts = 0
        # Enemy Reset
        enemy.x = 700
        enemy.y = 400
        enemy_walk_speed = 2
        attack_frames = 12
        enemy_health = 1
        # Health Reset
        life4 = uvage.from_image(130, 70, "HeartFull.png")
        life3 = uvage.from_image(165, 70, "HeartFull.png")
        life2 = uvage.from_image(200, 70, "HeartFull.png")
        life1 = uvage.from_image(235, 70, "HeartFull.png")
        life = {life1: True, life2: True, life3: True, life4: True}
        # Game Reset
        gameover = False
        score = 0
    # Scoring
    camera.draw(uvage.from_text(950, 70, str(int(score)), 70, "red", bold=False))


def tick():
    """
    This manages what happens each frame, it runs other functions each frame, which is currently 60
    :return:
    """
    camera.clear("light blue")
    create()
    if not gameover:
        walking()
        jumping()
        attack()
        enemies()
        defeated()
    camera.draw(character)
    camera.draw(enemy)
    health()
    hitboxes()
    knockback()
    game_over()
    camera.display()


uvage.timer_loop(60, tick)
