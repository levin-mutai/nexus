import { Component, OnInit } from '@angular/core';
import { ShopService } from '../services/shops/shop.service';
import { Router } from '@angular/router';
import { ShopCreateComponent } from './shop-create/shop-create.component';
import { MatDialog } from '@angular/material/dialog';
import { UserService } from '../services/users/user.service';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.scss'],
})
export class ShopComponent implements OnInit {
  all_shops: any[] = [];
  constructor(
    private shops: ShopService,
    private router: Router,
    public dialog: MatDialog,
    private user: UserService
  ) {}

  ngOnInit() {
    this.shops.getShops().subscribe((response) => {
      this.all_shops = response;
      console.log(this.all_shops);
    });
  }

  onCardClick(shopid: string) {
    console.log('clicked');
    this.router.navigate(['/shops/' + shopid]);
  }

  openDialog() {
    if (!this.user.isLoggedIn()) {
      this.router.navigate(['/login']);
    } else {
      const dialogRef = this.dialog.open(ShopCreateComponent, {
        height: '450px',
        width: '600px',
      });

      dialogRef.afterClosed().subscribe((result) => {
        console.log(`Dialog result: ${result}`);
      });
    }
  }
}
