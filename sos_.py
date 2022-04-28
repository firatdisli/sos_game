"""
9x9 Luk bir board üzerinde SOS
oyunu
1.Board görüntüle (Başlangıçta hepsi - olacak)
2.Play game
3.El değiştir, hamle yap
4.Check Win
    -satır kontrol
    -stun kontrol
    -çapraz kontrol
5. beraberlik kontrolü
6.oyuncu değiş
"""




# --------- Global Değişkenler -----------

# 9x9 luk board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# oyunu devam ettirmek için gerekli değişken
game_still_going = True

# Kazananı tutan değişken
winner = None

# Hamle yapacak oyuncu, başlangıçta X hamle yapacak
current_player = "S"


# ------------- Fonksiyonlar---------------

# Oyunun ana fonksiyonu
def play_game():

  # Boardı görüntüle
  display_board()

  # Kazanma veya beraberlik durumuna kadar çalışacak döngü
  while game_still_going:

    # Hamle yaptırma
    handle_turn(current_player)

    # Oyunun bitip bitmediğini kontrol etme
    check_if_game_over()

    # oyuncu değiştirme
    flip_player()
  
  # Kazananı yazdırma
  if winner == "S" or winner == "O":
    print(winner + " Kazandı.")
  elif winner == None:
    print("Beraberlik.")


# Oyun boardını gösterme
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


#hamle yapacak oyuncunun hamlesini kontrol eden fonksiyon
def handle_turn(player):

  # pozisyonu al
  print(player + "'in sırası.")
  position = input("1-9 arasında pozisyon seç: ")

  #Geçerli giriş kontrolü için
  valid = False
  while not valid:

    # Geçerli girişten emin olmak için
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("1-9 arasında pozisyon seç: ")
 
    # Board pozitionu index numarasından 1 fazladır
    position = int(position) - 1

    # Girilen pozisyonun geçerli olduğu kontrolü
    if board[position] == "-":
      valid = True
    else:
      print("Bu seçimi yapamazsın tekrar dene.")

  # Oyuncunun değeri boardın ilgili pozisyonuna yazılır X ya da O
  board[position] = player

  # Boardı görüntüle
  display_board()


# Oyun bitti mi
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Kimin kazandığının kontrolü
def check_for_winner():
  # Global değeri kullanmak gerekiyor
  global winner
  # Herhangi bir yerde kazanma durumu kontrolü
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Kazananı winner değerine atama
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# satırda kazanma var mı
def check_rows():
  # Global değişkeni kullanmak gerekiyor
  global game_still_going
  # satırların boş olup olmadığı kontrolü
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # Her hangi bir yerde eşleşme varsa, oyun devam etmez, 
  if row_1 or row_2 or row_3:
    game_still_going = False
  # kazananı gönder
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # yada beraberlik gönder
  else:
    return None


# sütunda kontrol
def check_columns():
  # Global değişkeni kullanmak gerekiyor
  global game_still_going
  # satırların boş olup olmadığı kontrolü
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # Her hangi bir yerde eşleşme varsa, oyun devam etmez,
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Kazananı gönder
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Beraberlik gönder, yani None
  else:
    return None


#  çapraz kontrol
def check_diagonals():
  # Global değişkeni kullanmak gerekiyor
  global game_still_going
  # satırların boş olup olmadığı kontrolü
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # Her hangi bir yerde eşleşme varsa, oyun devam etmez,
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Kazananı gönder
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Beraberlik gönder, yani None
  else:
    return None


# Beraberlik Kontrolü
def check_for_tie():
  # Global değişkeni kullan
  global game_still_going
  # Boardın Dolu olması gerekir, doluluk kontrolü
  if "-" not in board:
    game_still_going = False
    return True
  # Beraberlik yok
  else:
    return False


# Oyuncu Değiştirme S is O, O ise S yapılır
def flip_player():
  # Global değişkene ihtiyaç var
  global current_player
  # Mevcut oyuncu S ise
  if current_player == "S":
    current_player = "O"
  # Mevcut Oyuncu O ise S yapılır
  elif current_player == "O":
    current_player = "S"


# ------------ Oyunu Başlat -------------
# SOS Oyunu Oyna
play_game()