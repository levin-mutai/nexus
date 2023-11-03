import { NgModule, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductComponent } from './product/product.component';
import { ShopComponent } from './shop.component';
import { ShopdetailsComponent } from '../shopdetails/shopdetails.component';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';

@NgModule({
  declarations: [ProductComponent, ShopComponent, ShopdetailsComponent],
  imports: [CommonModule, MatCardModule, MatTableModule],
})
export class ShopModule {}
