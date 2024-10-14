import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Restaurant-new',
  templateUrl: './Restaurant-new.component.html',
  styleUrls: ['./Restaurant-new.component.scss']
})
export class RestaurantNewComponent {
  @ViewChild("RestaurantForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}