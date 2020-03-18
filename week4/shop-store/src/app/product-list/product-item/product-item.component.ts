import { Component, OnInit, Input } from '@angular/core';

import { products, Product } from '../../products';
// import { products, Product } from '../../products';
@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  @Input() product: Product;
  i:number = 1;
  constText:string = '';
  // text: string = product.img;
  text:string = '';
  constructor() { }

  ngOnInit(): void {
    this.constText = this.product.img;
    this.text = this.constText;
    console.log(this.text)
    this.text += this.i + '.jpg';
    this.product.img = this.text;

    setInterval(() => {
      console.log(this.constText);
      this.text = this.constText;
      this.i++;
      if(this.i == 4) this.i = 1;
      this.text += this.i + '.jpg';
      this.product.img = this.text;
    }, 3000);
  }

}
