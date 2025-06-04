import java.util.Scanner;

public class AverageCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double toplam = 0;
        int sayac = 0;

        System.out.println("Kaç not gireceksiniz?");
        int adet = input.nextInt();

        for (int i = 1; i <= adet; i++) {
            System.out.print(i + ". notu girin: ");
            double not = input.nextDouble();
            toplam += not;
            sayac++;
        }

        double ortalama = toplam / sayac;
        System.out.println("Not ortalamanız: " + ortalama);
    }
}
