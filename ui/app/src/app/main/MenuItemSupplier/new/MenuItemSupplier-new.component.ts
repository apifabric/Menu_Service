import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'MenuItemSupplier-new',
  templateUrl: './MenuItemSupplier-new.component.html',
  styleUrls: ['./MenuItemSupplier-new.component.scss']
})
export class MenuItemSupplierNewComponent {
  @ViewChild("MenuItemSupplierForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}