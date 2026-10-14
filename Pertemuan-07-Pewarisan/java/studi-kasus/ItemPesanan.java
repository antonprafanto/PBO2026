/** Satu baris pesanan: menu apa dan berapa porsi. */
public class ItemPesanan {
    private Menu menu;
    private int jumlah;

    public ItemPesanan(Menu menu, int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        this.menu = menu; // menyimpan REFERENSI ke objek Menu
        this.jumlah = jumlah;
    }

    public Menu getMenu() {
        return menu;
    }

    public int getJumlah() {
        return jumlah;
    }

    public int hitungSubtotal() {
        return menu.getHarga() * jumlah;
    }

    @Override
    public String toString() {
        return jumlah + " x " + menu.getNama();
    }
}
