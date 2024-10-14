import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './MenuItemPromotion-card.component.html',
  styleUrls: ['./MenuItemPromotion-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.MenuItemPromotion-card]': 'true'
  }
})

export class MenuItemPromotionCardComponent {


}