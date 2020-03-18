export interface Product {
  name: string,
  price: number,
  description: string,
  rating: number,
  img: string,
  url: string
}

export const products = [
    {
      name: 'Meizu Note 9',
      price: 55719.73,
      description: 'Глобальная версия Meizu Note 9 4 Гб 64 Гб 128 Гб Смартфон Snapdragon 675 Octa Core Note9 48MP двойная камера AI фронтальная 20 МП 4000 мАч',
      img: '../assets/images/phones/meizu-note-9_',
      rating: 4.9,
      url: 'https://aliexpress.ru/item/32972769104.html?spm=a2g0o.tm73743.8055123070.3.76a146b7B2jaWY&scm=1007.25281.150704.0&scm_id=1007.25281.150704.0&scm-url=1007.25281.150704.0&pvid=f696b60b-e496-4199-b742-9e6bb85d9337'
    },
    {
      name: 'Xiaomi Redmi 7',
      price: 46444.48,
      description: 'Смартфон Xiaomi Redmi 7 с глобальной прошивкой, 4 ГБ, 64 ГБ, Восьмиядерный процессор Snapdragon 632, полный экран 6,26 дюйма, камера 12 МП, аккумулятор 4000 мАч, Redmi7',
      img: '../assets/images/phones/xiaomi-redmi-7_',
      rating: 4.9,
      url: 'https://aliexpress.ru/item/32990522944.html?spm=a2g0o.tm73743.8055123070.3.76a146b7nI0LZt&scm=1007.25281.150704.0&scm_id=1007.25281.150704.0&scm-url=1007.25281.150704.0&pvid=d6aad5ca-05f3-4638-8cf6-d004185c8611'
    },
    {
      name: 'Apple iPhone 11',
      price: 319915.04,
      description: 'Смартфон Apple iPhone 11 64GB [официальная гарантия, "ростест", быстрая доставка от 1 дня]',
      img: '../assets/images/phones/apple-iphone-11_',
      rating: 4.9,
      url: 'https://tmall.ru/item/Apple-iPhone-11-64GB/4000171735887.html?productId=4000171735887&spm=a2g0o.productlist.0.0.29b6143aOsuwvo&algo_pvid=c99377f7-e790-4398-9072-ffdd0c11f6e7&algo_expid=c99377f7-e790-4398-9072-ffdd0c11f6e7-12&btsid=77192cb9-bb4f-4e41-bb63-9209e3549fdc&ws_ab_test=searchweb0_0,searchweb201602_6,searchweb201603_55'
    },
    {
      name: 'OBD2',
      price: 15042.33,
      description: 'OBD2 автомобильный сканер, считыватель данных в режиме реального времени, код двигателя, диагностический инструмент ANCEL AD310',
      img: '../assets/images/phones/obd2_',
      rating: 0,
      url: 'https://aliexpress.ru/item/4000146085201.html?spm=a2g0v.best.6.7.9b6a5xFw5xFwH9&scm=1007.17258.156310.0&pvid=a90f9b01-0853-41c6-92ae-eec131dea9d5'
    }
  ];
  
  
  /*
  Copyright Google LLC. All Rights Reserved.
  Use of this source code is governed by an MIT-style license that
  can be found in the LICENSE file at http://angular.io/license
  */