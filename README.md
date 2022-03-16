# turkce_isimlerden_cinsiyet_belirleme
Türkçe isimler bulunan bir listede, hangi cinsiyetten kaç adet birey olduğunun belirlenmesine yarayan bir python kodu. 
Bu kod için türkçe isimler veritabanı olarak https://gist.github.com/ismailbaskin/1325813/9157dd8ced294a11218449d43bf9f772780f5d85 adresindeki isim ve cinsiyet listesi kullanılmıştır.
İlgili liste öncelikle bir python listesine dönüştürüldü. Ardından isimlerin cinsiyetlerini "1: erkek, 2: kadın, 3: unisex ve 4: bilinmeyen" olarak ayıran bir fonksiyon yazıldı.
Fonksiyon çıktı olarak isimlerin cinsiyetlere göre dağılımını 1, 2, 3 ve 4 olarak kodlayan bir sözlük olan gender_dict'i oluşturur. Buradaki sınıflandırma kesin olmakla birlikte 3 ve 4 cinsiyeti ayırt edilemeyen isimlerin sayısıdır. 
Bu aşamadan sonra kesin olmasa da tahmini olarak bütün isimleri erkek ve kadın yani 1 ve 2 olarak sınıflandıran "estimated_dict" sözlüğü oluşturuldu. Burada öncelikle ilk oluşturulan sözlükteki unisex isimler ve cinsiyeti belirlenemeyen isimler toplandı. Bu toplam rakam yine ilk sözlükteki 1 ve 2'ye göre oransal olarak dağıtıldı. Burada bahsedilen oranlar gender_dict'teki 1 ve 2'nin birbirine olan oranlarıdır. Daha kolay anlaşılması için seçim anketlerinde kararsızların dağıtılması prensibine benzer bir prensip izlenmiş oldu.
Test dosyasında rastgele isimler liste şeklinde sıralanarak fonksiyonun buradaki isimlerin cinsiyetlerini belirlemesi sağlandı. Kendi verilerini test etmek isteyen arkadaşlar "test" dosyasındaki listeye kendi listelerini ekleyerek cinsiyet dağılımını hesaplayabilirler. 

A python code for determining how many individuals of which gender are in a list with Turkish names. For this code, the name and gender list at https://gist.github.com/ismailbaskin/1325813/9157dd8ced294a11218449d43bf9f772780f5d85 is used as a database of Turkish names. 
The relevant list was first converted to a python list. Then a function was written that separated the genders of the nouns into "1: male, 2: female, 3: unisex, and 4: unknown". The function outputs gender_dict, a dictionary that encodes the distribution of names by gender as 1, 2, 3, and 4. Although the classification here is precise, 3 and 4 are the number of nouns whose gender cannot be distinguished. 
After this stage, the "estimated_dict" dictionary was created, which classifies all names as male and female, ie 1 and 2, although it is not certain. First of all, unisex nouns and nouns whose gender cannot be determined in the first dictionary were collected. 
This total number was distributed proportionally according to 1 and 2 in the first dictionary. 
The ratios mentioned here are the ratios of 1 and 2 in gender_dict to each other. For easier understanding, a principle similar to the principle of distributing the undecided was followed in the election polls. 
In the test file, random names were listed as a list, and the function was allowed to determine the gender of the names here. If you want to test your own data, you can calculate the gender distribution by adding your own list to the list in the "test" file.
