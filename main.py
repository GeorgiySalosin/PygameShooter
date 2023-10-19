import pygame
import atlas
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BG = (165, 165, 165)



#player actions
movingLeft = False
movingRight = False

#player binding pose
poseStand = True
poseCrouch = False
poseProne = False
poseList = ('Stand', 'Crouch', 'Prone')
currentPose = 0


class Avatar(pygame.sprite.Sprite):
    def __init__(self, x, y, avatar_gender, avatar_type, avatar_scale, avatar_speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.gender = avatar_gender
        self.type_avatar = avatar_type
        self.scale_avatar = avatar_scale
        self.speed_avatar = avatar_speed
        self.direction_avatar = 1
        self.flip_avatar = False
        self.avatar_pose = poseList[0]
        img_avatar = pygame.image.load(f'Content/Character/{self.gender}/{self.type_avatar}/Base/{self.avatar_pose}_Base.png')
        self.img_avatar = pygame.transform.scale(img_avatar, (int(img_avatar.get_width() * self.scale_avatar), int(img_avatar.get_height() * self.scale_avatar)))
        self.rect_avatar = self.img_avatar.get_rect()
        self.rect_avatar.center = (self.x, self.y)
    def draw(self):
        screen.blit(pygame.transform.flip(self.img_avatar, self.flip_avatar, False), self.rect_avatar)
    def change_pose(self, pose_from_list):
        global currentPose
        currentPose = pose_from_list
        self.avatar_pose = poseList[pose_from_list]
        self.img_avatar = pygame.image.load(f'Content/Character/{self.gender}/{self.type_avatar}/Base/{self.avatar_pose}_Base.png')
        self.img_avatar = pygame.transform.scale(self.img_avatar, (int(self.img_avatar.get_width() * self.scale_avatar), int(self.img_avatar.get_height() * self.scale_avatar)))
        if pose_from_list == 0:
            self.poseStand = True
            self.poseCrouch = False
            self.poseProne = False
        elif pose_from_list == 1:
            self.poseStand = False
            self.poseCrouch = True
            self.poseProne = False
        elif pose_from_list == 2:
            self.poseStand = False
            self.poseCrouch = False
            self.poseProne = True

    def move(self):
        dx = 0
        dy = 0
        if movingLeft:
            dx -= self.speed_avatar
            self.direction_avatar = 0
            self.flip_avatar = True
        if movingRight:
            dx += self.speed_avatar
            self.direction_avatar = 1
            self.flip_avatar = False
        self.rect_avatar.x += dx
        self.rect_avatar.y += dy

player = Avatar(500, 700, 'Male', 'Nude', 0.5, 5)


run = True
while run:
    screen.fill(BG)
    screen.blit(atlas.tree01_2, (0,0))
    player.draw()
    player.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #KEYDOWN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_a:
                movingLeft = True
            if event.key == pygame.K_d:
                movingRight = True
            if event.key == pygame.K_w:
                player.change_pose(0)
            if event.key == pygame.K_s:
                player.change_pose(1)
            if event.key == pygame.K_z:
                player.change_pose(2)

    # KEYUP
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_a:
                movingLeft = False
            if event.key == pygame.K_d:
                movingRight = False
    pygame.display.flip()
pygame.quit()
quit()
