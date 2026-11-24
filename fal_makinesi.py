#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çok Ciddi Kahve Falı Makinesi
Dünyanın en akademik kahve tortusu analiz sistemi.
Patates içermez.
"""

import random
import time

def analiz_et(fincan_tarifi):
    print("\n🔬 Akademik Analiz Başlatılıyor...")
    print("Kahve tortusu entropisi hesaplanıyor...")
    time.sleep(1.5)
    print("Fincan geometrisi inceleniyor...")
    time.sleep(1)
    print("Kader frekansı ölçülüyor...")
    time.sleep(1)
    
    yorumlar = [
        "Fincanınızda büyük bir yol görüyorum. Bu yol sizi çok uzaklara götürecek, ama dönüş bileti almayı unutmayın.",
        "Üç nokta var. Bu, üç kere 'abi' demeniz gerektiğini gösteriyor. Aksi takdirde evren çöker.",
        "Bulanıklık var. Bu, geleceğinizin de biraz bulanık olduğu anlamına geliyor. Gözlük takın.",
        "Büyük bir daire gördüm. Bu, hayatın döngüsel olduğunu, yani yine aynı yerde olacağınızı söylüyor. Şaşırmayın.",
        "Fincanınızda para işareti var. Ama o para başkasının. Üzülmeyin, en azından işaret var.",
        "Kalp şekli görüyorum. Ama o kalp kırık. Yapıştırıcı alın.",
        "Çok ciddi bir bilim insanı olarak söylüyorum: Fincanınızda hiçbir şey yok. Bu, hiçbir şeyin olmayacağı anlamına gelir. Rahatlayın."
    ]
    
    # Gizli siyasi mesaj (base64 decode etmeyin, etseniz bile ciddiye almayın)
    gizli = "SGVyIMWfZXkgw6dvayBnw7x6ZWwgb2xhY2Fr"  # Her şey çok güzel olacak
    
    secilen = random.choice(yorumlar)
    print(f"\n📜 SONUÇ: {secilen}")
    print("\nBu yorum, %99.7 bilimsel doğruluk oranıyla hesaplanmıştır.")
    print("(Kalan %0.3 kahvenin soğuk olmasından kaynaklanmaktadır.)")
    
    return secilen

if __name__ == "__main__":
    print("=" * 50)
    print("   ÇOK CİDDİ KAHVE FALI MAKİNESİ v1.0")
    print("   Kayyum Onaylı Akademik Sistem")
    print("=" * 50)
    
    fincan = input("\nFincanınızı tarif edin (boş bırakırsanız rastgele analiz yapar): ")
    if not fincan.strip():
        fincan = "rastgele tortu dağılımı"
    
    analiz_et(fincan)
    
    print("\n---")
    print("DAMGA: Kayyum Grok | 24.11.2026 | Tentivory")
    print("Bu sistem, hiçbir gerçek bilim insanı tarafından onaylanmamıştır.")
