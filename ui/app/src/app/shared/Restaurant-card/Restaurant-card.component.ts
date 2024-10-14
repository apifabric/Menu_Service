import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Restaurant-card.component.html',
  styleUrls: ['./Restaurant-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Restaurant-card]': 'true'
  }
})

export class RestaurantCardComponent {


}