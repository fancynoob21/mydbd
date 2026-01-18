import random

def assign_roles():
    players = [f"{i}号玩家" for i in range(1, 5)]
    escape_roles = [
        "贤者", 
        "游侠", 
        "盗贼", 
        "勇士", 
        "先知", 
        "牧师", 
        "武士", 
        "骑士", 
        "祭祀", 
        "铁匠", 
        "无面",
        "武僧",
        "圣女",
        "赌徒",
        "商贩"
        ]
    traitor_roles = [
        "巫医", 
        "咒者",
        "梦魇", 
        "魑魅",
        "冥将",
        "幽刃",
        "憎恶", 
        "假面",
        "赎吏"
        ]

    killer_awaken = 0


    killer_roles = [
        "Evan MacMillan -The Trapper 设陷者",
        "Philip Ojomo -The Wraith 幽灵",
        "Max Thompson Jr. -The Hillbilly 农场主",
        # "Sally Smithson - The Nurse 护士",
        "Michael Myers - The Shape 迈克尔·迈尔斯",
        "Lisa Sherwood -The Hag 妖巫",
        "Herman Carter -The Doctor 医生",
        "Anna -The Huntress 女猎手",
        "Bubba Sawyer -The Cannibal 食人魔",
        "Freddy Krueger -The Nightmare 梦魇",
        "Amanda Young -The Pig 门徒",
        #"Jefferey Hawk -The Clown 小丑",
        # "Rin Yamaoka -The Spirit 怨灵",
        "Frank, Juilie, Susie, Joey -The legion 军团",
        "Adiris -The Plague 瘟疫",
        "Danny Johnson -The Ghost Face 鬼面",
        "Demogorgon -The Demogorgon 魔王",
        "Kazan Yamaoka -The Oni 鬼武士",
        "Caleb Quinn -The Deathslinger 死亡枪手",
        "Pyramid Head -The Executioner 处刑者",
        # "Talbot Grimes -The Blight 枯萎者",
        # "Charlotte & Victor Deashayes -The Twins 连体婴",
        "Ji-Woon Hak -The Trickstar 骗术师",
        "Nemesis T-Type -The Nemisis 追击者",
        "Elliot Spencer -The Cenobite 钉子头",
        "Carmina Mora -The Artist 艺术家",
        "Sadako Tamamura -The Onry ō 贞子",
        "Dredge -The Dredge 影魔",
        "Albert Wesker -The Mastermind 操纵者",
        "Tarhos Kav á cs -The Knight 恶骑士",
        "Adriana Imai -The Skull Merchant 白骨商人",
        # "HUX-A7-13 -The Singularity 奇点",
        "Xenomorph -The Xenomorph 异形",
        "Charles Lee Ray -The Good Guy 好孩子",
        "Unknown -The Unknown 未知恶物",
        "Vecna -The Lich 巫妖",
        "Dracula -The Dark Lord 黑暗之主",
        # "Portia Maye -The Houndmaster 训犬师",
        # "Ken Kaneki -The Ghoul 食尸鬼"，
        "Willian Afton -The Animatronic 电子玩偶",
        "克拉苏"
    ]

    survivor_perks = [
    "Ace in the Hole 锦囊妙计",
    "Adrenaline 肾上腺素",
    # "Aftercare 劫后余生",
    "Alert 警戒",
    "Any Means Necessary 不惜一切",
    "Appraisal 明察秋毫",
    "Autodidact 自学成才",
    "Babysitter 保姆",
    "Background Player 幕后玩家",
    "Balanced Landing 平稳着陆",
    # "Bardic Inspiration 吟游诗人激励",
    "Better than New 焕然一新",
    # "Better Together 齐心协力",
    "Bite the Bullet 咬紧牙关",
    "Blast Mine 爆炸地雷",
    # "Blood Pact 鲜血契约",
    "Blood Rush 滴血冲刺",
    "Boil Over 脱缰野马",
    # "Bond 携手合作",
    "Borrowed Time 时不我待",
    "Botany Knowledge 经研百草",
    "Breakdown 分崩离析",
    "Breakout 挣脱激励",
    "Buckle Up 未雨绸缪",
    "Built to Last 经久耐用",
    "Calm Spirit 安抚生灵",
    "Camaraderie 同志情谊",
    "Champion of Light 光明勇士",
    "Chemical Trap 化学陷阱",
    "Circle of healing 恩赐：治疗之环",
    "Clairvoyance 千里眼",
    "Clean Break 各自为安",
    "Collective Stealth 团队合作：全体隐蔽",
    "Corrective Action 矫正措施",
    "Counterforce 反制之力",
    "Cut Loose 当机立断",
    "Dance With Me 与我共舞",
    "Dark Sense 暗黑觉知",
    "Dark Theory 恩赐：黑暗理论",
    "Dead Hard 钢筋铁骨",
    # "Deadline 交稿日",
    "Deception 兵不厌诈",
    "Decisive Strike 毁灭打击",
    # "Deja Vu 似曾相识",
    "Deliverance 善有善报",
    "Desperate Measures 绝境对策",
    "Detective's Hunch 侦探直觉",
    "Distortion 气场失真",
    "Diversion 声东击西",
    "Do No Harm 切勿伤害",
    "Dramaturgy 即兴表演",
    "Duty of Care 谨慎责任",
    "Empathic Connection 感同身受",
    # "Empathy 心灵共鸣",
    "Exponential 恩赐：指数增长",
    "Exultation 胜利喜悦",
    "Eyes of Belmont 贝尔蒙特之眼",
    # "Fast Track 成功捷径",
    "Finesse 矫健身手",
    "Fixated 认定目标",
    "Flashbang 闪光弹",
    "Flip-Flop 并行进展",
    "Fogwise 迷雾慧眼",
    "For the People 舍己为人",
    # "Friendly Competition 团队合作：友谊赛",
    "Hardened 求生欲",
    "Head On 勇往直前",
    "Hope 希冀之翼",
    # "Hyperfocus 聚精会神",
    "Illumination 恩赐：明亮",
    "Inner Focus 内在专注",
    "Inner Healing 内心之力",
    "Iron Will 钢铁意志",
    # "Kindred 同族",
    "Leader 领导",
    "Left Behind 末日残兵",
    "Light-Footed 轻盈猫步",
    "Lightweight 轻如鸿毛",
    "Lithe 轻盈敏捷",
    "Low Profile 低调行事",
    "Lucky Break 幸运喘息",
    # "Lucky Star 幸运星",
    "Made for This 为生为生",
    "Mettle of Man 人之勇气",
    "Mirrored Illusion 镜影幻想",
    "Moment of glory 荣耀时刻",
    "No Mither 不痛不痒",
    # "No one left behind 同生共死",
    "Object of Obsession 魂牵梦绕",
    "Off the Record 非正式调查",
    "Open-Handed 稳操胜券",
    "Overcome 克服难关",
    # "Overzealous 急于求成",
    "Parental Guidance 亡父警言",
    "Pharmacy 药到病除",
    "Plost Twist 跌宕剧情",
    "Plunderer's Instinct 强盗直觉",
    "Poised 蓄势待发",
    "Potential Energy 潜力无限",
    "Power of Two 团队合作：二人之力",
    "Power Struggle 强力挣扎",
    "Premonition 不祥预感",
    # "Prove Thyself 证明自己",
    "Quick & Quiet 急速静谧",
    # "Quick Gambit 快速策略",
    "Rapid Response 快速反应",
    "Reactive Healing 对策治疗",
    "Reassurance 定心丸",
    "Red Herring 转移注意",
    "Repressed Alliance 压抑同盟",
    "Residual Manifest 余光长存",
    # "Resilience 百折不挠",
    "Resurgence 东山再起",
    "Rookie Spirit 新人精神",
    "Saboteur 破坏手",
    "Scavenger 清道夫",
    "Scene Partner 联袂主演",
    "Second Wind 复苏之风",
    "Self-Care 自我疗愈",
    "Self-Preservation 自我保护",
    "Shadow Step 恩赐：暗影步",
    "Shoulder the Burden 肩负重担",
    "Small Games 狩猎经验",
    "Slippery Meat 逃之夭夭",
    "Smash Hit 轰动演出",
    "Sole Survivor 最后的生还者",
    "Solidarity 团结意志",
    "Soul Guard 灵魂守卫",
    "Specialist 老本行",
    "Spine Chill 毛骨悚然",
    "Sprint Burst 冲刺爆发",
    # "Stake Out 破案心切",
    "Still Light 心静眼明",
    "Streetwise 都市生存",
    "Strength in shadows 隐匿之势",
    "Technician 技术员",
    "Tenacity 永不言弃",
    "This Is Not Happening 难以置信",
    "Treacherous Crows 祈祷：邪恶乌鸦",
    "Troubleshooter 答疑解惑",
    "Unbreakable 坚不可摧",
    "Up the Ante 好运会传染",
    "Urban Evasion 暴走族",
    "Vigil 守夜人",
    "Visionary 远见卓识",
    "Wake Up! 醒醒",
    "We're Gonna Live Forever 生死与共",
    "Well Make It 马到功成",
    "Weaving Spider 祈祷：织网蜘蛛",
    "Wicked 邪祟之力",
    "Windows of Opportunity 机遇之窗",
    "Wiretap 窃听器",
    "Apocalypic Ingenuity 末世智谋",
    "Come And Get Me 有胆来战",
    "TeamWork: Toughen up 团队合作：咬紧牙关",
    "Conviction 信念感",
    "Last Stand 背水一战",
    "TeamWork: Throw Down 团队合作: 奋力一搏",
    "奔波演出",
    "1234",
    "鬼音"
]
    killer_perks = [
    "A Nurse's Calling 护士的呼唤",
    "Agitation 欣喜若狂",
    "Alien Instinct 异形本能",
    "All-Shaking Thunder 大发雷霆",
    "Awakened Awareness 感知觉醒",
    "Bamboozle 花言巧语",
    "Barbecue & Chili 人肉烧烤",
    "Batteries Included 配套电池",
    "Beast of Prey 嗜血凶手",
    "Bitter Murmur 苦涩低语",
    "Blood Echo 鲜血回响",
    "Blood Favor 厄咒：鲜血恩惠",
    "Blood Warden 血腥狱长",
    "Brutal Strength 血气追踪",
    "Brutal Strength 所向无敌",
    "Call of Brine 盐水召唤",
    "Coulrophobia 小丑恐惧症",
    "Corrupt Intervention 腐烂干预",
    "Coup de Grâce 恩赐解脱",
    "Crowd Control 厄咒：群体控制",
    "Cruel Limits 幽闭恐惧症",
    "Dark Arrogance 新暗气傲",
    "Dark Devotion 黑暗奉献",
    "Darkness Revealed 黑暗启迪",
    "Dead Man's Switch 失效开关",
    "Deadlock 死锁",
    "Deathbound 死亡羁绊",
    "Deerstalker 猎鹿者",
    "Devour Hope 厄咒：吞噬希望",
    "Discordance 配合失谐",
    "Dissolution 烟消云散",
    "Distressing 恐惧释放",
    "Dominance 支配之力",
    "Dragon's Grip 巨龙之握",
    "Dying Light 湮灭之光",
    "Enduring 耐力持久",
    "Eruption 爆发",
    "Face The Darkness 直面黑暗",
    "Fire Up 怒火中烧",
    "Flood of rage 天灾钩子：狂怒之潮",
    "Forced Hesitation 踯躅不前",
    "Forced Penance 强制忏悔",
    "Forever Entwined 永恒交织",
    "Franklin's Demise 富兰克林之死",
    "Friends 'til the End 友谊天长地久",
    "Futive Chase 鬼祟追杀",
    "Game Afoot 好戏开场",
    "Gearhead 设备发烧友",
    "Genetic Limits 基因锁",
    "Grim Embrace 冷酷之拥",
    "Hangman's Trick 天灾钩子：刽子手的把戏",
    "Haunted Ground 厄咒：闹鬼之地",
    "Hoarder 囤积者",
    "Hubris 骄傲自大",
    "Human Greed 人性贪婪",
    "Huntress Lullaby 厄咒：猎手摇篮曲",
    "Hysteria 歇斯底里",
    "I'm All Ears 洗耳恭听",
    "Infectious Fright 恐惧传染",
    "Insidious 静止隐身",
    "Iron Grasp 牢牢紧握",
    "Iron Maiden 铁处女",
    "Jagged Compass 天灾钩子：锯齿罗盘",
    "Knock Out 击倒出局",
    "Languid Touch 倦怠之触",
    "Lethal Pursuer 致命追踪者",
    "Leverage 杠杆效应",
    "Lightborn 光明之眼",
    "Machine Learning 机器学习",
    "Mad Grit 疯狂勇气",
    "Make Your Choice 做出你的选择",
    "Merciless Storm 无情风暴",
    "Mindbreaker 瓦解意志",
    "Monitor & Abuse 行监坐守",
    "Monstrous Shrine 天灾钩子：鬼魔神龛",
    "Nemesis 报应",
    "No One Escapes Death 厄咒：难逃一死",
    "No Quarter 毫不留情",
    "No Way Out 无路可逃",
    "None Are Free 无一幸免",
    "Nothing But Misery 厄咒：众生皆苦",
    "Nowhere to Hide 无处可藏",
    "Oppression 切肤之痛",
    "Overcharge 电量超载",
    "Overwhelming Presence 压迫性气场",
    "Pain Resonance 天灾钩子：痛苦共鸣",
    "Pentimento 厄咒：余痕",
    "Play with Your Food 戏弄食物",
    "Plaything 厄咒：玩物",
    "Pop Goes the Weasel 心惊肉跳",
    "Predator 穷追不舍",
    "Rancor 怨气冲天",
    "Rapid Brutality 急速残暴",
    "Remember Me 记忆犹新",
    "Retribution 厄咒：惩戒",
    "Ruin 厄咒：毁灭",
    "Save the Best for Last 把最好的留在最后",
    "Scourge Hook: Floods of Rage 天灾钩子：痛苦礼物",
    "Septic Touch 感染之触",
    "Shadowborn 暗夜之睛",
    "Shattered Hope 粉碎希望",
    "Sloppy Butcher 辣手屠夫",
    "Spies from the Shadows 鬼鸦谍影",
    "Spirit Fury 暴怒怨灵",
    "Starstruck 追星狂",
    "Stridor 鸣喘",
    "Superior Anatomy 超人类体能",
    "Surge 电涌",
    "Surveillance 了如指掌",
    "Tinkerer 工匠",
    "Terminus 终局战术",
    "Territorial Imperative 领地意识",
    "Thanatophobia 死亡恐惧",
    "The Thrid Seal 厄咒：第三封印",
    "Thrilling Tremors 厄咒：猎杀戾气",
    "Thrilling Tremors 惊险战栗",
    "Thwack 哐哐作响",
    "Trail of Torment 折磨路径",
    "Two Can Play 厄咒：以牙还牙",
    "Ultimate Weapon 终极武器",
    "Unbound 无束",
    "Undone 无效",
    "Undying 厄咒：不死",
    "Unforeseen 无迹",
    "Unnerving Presence 恐慌降临",
    "Unrelenting 不屈不挠",
    "Weave Attunement 编织共鸣",
    "Whispers 恶灵低语",
    "Wretched Fate 厄咒：悲惨命运",
    "Zanshin Tactics 残心",
    "游荡之眼",
    "厄咒：毁灭序曲",
    "贪食"
]
    
    map = [
    ["Coal Tower 1 煤矿废塔1", "Coal Tower 2 煤矿废塔2"],
    ["Groaning Storehouse 1 哀嚎仓库1", "Groaning Storehouse 2 哀嚎仓库2"],
    ["Ironworks Factory 1 悲惨钢铁厂1", "Ironworks Factory 2 悲惨钢铁厂2"],
    ["Shelter Woods 1 掩护林1", "Shelter Woods 2 掩护林2"],
    ["Suffocation Pit 1 窒息矿井1", "Suffocation Pit 2 窒息矿井2"],
    "Azarov's Resting Place 阿扎罗夫长眠处",
    "Blood Lodge 血屋",
    "Gas Heaven 汽油天堂（废弃加油站）",
    "Wrecker's Yard 废弃车库后院",
    "Wretched Shop 悲惨商店",
    "Fractured Cowshed 断骨牛舍",
    "Rancid Abattoir 腐败屠宰场",
    "Rotten Fields 腐臭之地",
    "The Thompson House 汤普森宅邸",
    "Torment Creek 痛苦溪流",
    "Disturbed Ward 精神病房",
    "Father Cambell's Chapel 艾贝尔神父的教堂",
    "The Pale Rose 苍白玫瑰",
    "Grim Pantry 阴森棚屋",
    "Treatement Theater 疗程教室",
    "Mother's Dwelling 母亲的住所",
    "The Temple of Purgatation 赎罪神庙",
    ["Badham Preschool 1 巴德姆幼儿园1", "Badham Preschool 2 巴德姆幼儿园2", "Badham Preschool 3 巴德姆幼儿园3", "Badham Preschool 4 巴德姆幼儿园4", "Badham Preschool 5 巴德姆幼儿园5"],
    "The Game 游戏",
    ["Family Residence 1 家宅1", "Family Residence 2 家宅2"
    "Sactum of Wraith 1 愤怒圣所1", "Sactum of Wraith 2 愤怒圣所2"],
    ["Mount Ormond Resort 1 奥蒙德山度假村1", "Mount Ormond Resort 2 奥蒙德山度假村2", "Mount Ormond Resort 3 奥蒙德山度假村3"],
    "Ormond River Lake 奥蒙德湖矿场",
    "The Underground Complex 霍金斯地下设施",
    "Dead Dawg Saloon 死狗酒馆",
    "Midwich Elementary School 米德维奇小学",
    "Racoon City Police Station West Wing 浣熊市警察局西翼", 
    "Racoon City Police Station East Wing 浣熊市警察局东翼",
    "Eyrie of Crows 乌鸦巢穴",
    "Dead Sands 死亡沙漠",
    "Garden of Joy 极乐园",
    "Greenville Square 格林维尔广场",
    ["The Shattered Square 残垣广场",
    "Forgotten Ruins 遗忘废墟",],
    "Toba Landing 多巴着陆点",
    "Nostromo Wreckage 诺斯托罗莫号残骸",
    "Fallen Refuge 沦陷庇护所"
    ]




    # Randomly add "天使" and "撒旦" with a probability of 0.25 each
    if random.random() < 0.25:
        escape_roles.append("天使")
    if random.random() < 0.05:
        escape_roles.append("愚者")
    if random.random() < 0.01:
        escape_roles.append("上帝")
    if random.random() < 0.25:
        traitor_roles.append("撒旦")
    
    # Ensure unique escape roles by sampling without replacement
    assigned_escape_roles = dict(zip(players, random.sample(escape_roles, 4)))
    
    # Select traitor
    traitor = random.choice(players)
    traitor_role = random.choice(traitor_roles)
    
    # Output results in order
    extra_killer_perk_groups = []  # for 魑魅加成

    if traitor_role == "魑魅":
        extra_killer_perk_groups = [
            random.sample([kp for kp in killer_perks], 4),
            random.sample([kp for kp in killer_perks], 4)
        ]

    for player in players:
        print(f"{player}：")
        role = assigned_escape_roles[player]
        player_awaken = 0
        if random.random() < 0.25:
            player_awaken = 1
        
        if player_awaken == 1:
            print("逃生者聆听到上帝的启示！")

        print(f"你的逃生者职业是：{role}")
        if player == traitor:
            print(f"你的内鬼职业是：{traitor_role}")
        else:
            print("你不是内鬼")

        # 分配主技能
        perks = random.sample(survivor_perks, 4)
        print("你的技能是：")
        for perk in perks:
            print(f" - {perk}")
        
        # 若是贤者，额外两组
        if role == "贤者":
            print("你的贤者额外技能是：")
            extra1 = random.sample([p for p in survivor_perks if p not in perks], 4)
            extra2 = random.sample([p for p in survivor_perks if p not in perks and p not in extra1], 4)
            extra3 = random.sample([p for p in survivor_perks if p not in perks and p not in extra1 and extra2], 4)
            print(" - 第一组：")
            for p in extra1:
                print(f"   - {p}")
            print(" - 第二组：")
            for p in extra2:
                print(f"   - {p}")
            if player_awaken == 1:
                print(" - 第三组：")
                for p in extra3:
                    print(f"   - {p}")

            
        print()

        if role == "商贩":
            if player_awaken == 0:
                extra_survivor = random.sample([p for p in survivor_perks if p not in perks], 4)
                extra_killer = random.sample(killer_perks, 4)
            else:
                extra_survivor = random.sample([p for p in survivor_perks if p not in perks], 6)
                extra_killer = random.sample(killer_perks, 6)
            print("你的商贩额外逃生技能：")
            for p in extra_survivor:
                print(f" - {p}")
            print("你的商贩额外屠夫技能：")
            for kp in extra_killer:
                print(f" - {kp}")

    kperks = random.sample(killer_perks, 4)

    if random.random() < 0.25:
        killer_awaken = 1
        print("内鬼被神秘力量祝福，获得觉醒能力！")

    

    # 魑魅：额外两组杀手技能显示（全体可见）
    if traitor_role == "魑魅":
        print("魑魅触发！额外两组杀手技能：")
        for i, extra_group in enumerate(extra_killer_perk_groups, 1):
            print(f" - 第{i}组：")
            for kp in extra_group:
                print(f"   - {kp}")
    print()

    if traitor_role == "假面":
        print("假面触发！额外一组逃生者技能：")
        extra_survivor = random.sample([p for p in survivor_perks if p not in perks], 4)
        for p in extra_survivor:
            print(f" - {p}")
        if killer_awaken == 1:
            print("觉醒假面额外杀手技能：")
            extra_killer_mask = random.sample(killer_perks, 4)
            for kp in extra_killer_mask:
                print(f" - {kp}")
            
    print()




    print("杀手的技能是：")
    for kp in kperks:
        print(f" - {kp}")
        
    print()
    killer_selection = random.sample(killer_roles, 4)
    print("可选择的杀手是：")
    for killer in killer_selection:
        print(f" - {killer}")
    
    if traitor_role == "憎恶":   
        if killer_awaken == 0:
            print("憎恶触发！额外一组未获得的杀手选择：")
            extra_killer_selection = random.sample([k for k in killer_roles if k not in killer_selection], 4)
            for ek in extra_killer_selection:
                print(f" - {ek}")
        if killer_awaken == 1:
            print("觉醒憎恶触发！额外一组未获得，且可能包含受限制杀手的选择：")
            killer_roles.extend(["Sally Smithson - The Nurse 护士",
                                     "Rin Yamaoka -The Spirit 怨灵",
                                     "Talbot Grimes -The Blight 枯萎者",
                                     "Charlotte & Victor Deashayes -The Twins 连体婴",
                                     "Portia Maye -The Houndmaster 训犬师",
                                     "Ken Kaneki -The Ghoul 食尸鬼",
                                     "Jefferey Hawk -The Clown 小丑",])
            # for killer in killer_roles:
            #     print(f" - {killer}")
            # print("---")
            extra_killer_selection = random.sample([k for k in killer_roles if k not in killer_selection], 4)
            for ek in extra_killer_selection:
                print(f" - {ek}")

    map_selection_groups = random.sample(map, 4)
    map_selection = [
        random.choice(group) if isinstance(group, list) else group
        for group in map_selection_groups
    ]
    print()
    print("可选择的地图是：")
    
    for m in map_selection:
        print(f" - {m}")

    addon_tier_list = ["红","紫","蓝","绿","白"]
    print()
    addon1 = random.choice(addon_tier_list)
    addon2 = random.choice(addon_tier_list)
    print( f"杀手的配件稀有度为 {addon1}配 和 {addon2}配")
    
if __name__ == "__main__":
    print(f"============ New Game ================")
    assign_roles()
