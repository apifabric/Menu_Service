import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'MenuItemPromotion-new',
  templateUrl: './MenuItemPromotion-new.component.html',
  styleUrls: ['./MenuItemPromotion-new.component.scss']
})
export class MenuItemPromotionNewComponent {
  @ViewChild("MenuItemPromotionForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}