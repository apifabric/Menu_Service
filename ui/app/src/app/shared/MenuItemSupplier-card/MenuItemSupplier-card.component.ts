import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './MenuItemSupplier-card.component.html',
  styleUrls: ['./MenuItemSupplier-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.MenuItemSupplier-card]': 'true'
  }
})

export class MenuItemSupplierCardComponent {


}