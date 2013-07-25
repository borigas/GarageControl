# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Relay'
        db.create_table(u'garage_app_relay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relayPin', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('garage_app', ['Relay'])

        # Adding model 'Sensor'
        db.create_table(u'garage_app_sensor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('triggerPin', self.gf('django.db.models.fields.IntegerField')()),
            ('echoPin', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('garage_app', ['Sensor'])

        # Adding model 'Led'
        db.create_table(u'garage_app_led', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pin', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('garage_app', ['Led'])

        # Adding model 'RgbLed'
        db.create_table(u'garage_app_rgbled', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('redLed', self.gf('django.db.models.fields.related.ForeignKey')(related_name='redLed', to=orm['garage_app.Led'])),
            ('greenLed', self.gf('django.db.models.fields.related.ForeignKey')(related_name='greenLed', to=orm['garage_app.Led'])),
            ('blueLed', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blueLed', to=orm['garage_app.Led'])),
        ))
        db.send_create_signal('garage_app', ['RgbLed'])

        # Adding model 'Door'
        db.create_table(u'garage_app_door', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('relay', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['garage_app.Relay'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['garage_app.Sensor'])),
            ('rgbLed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['garage_app.RgbLed'])),
        ))
        db.send_create_signal('garage_app', ['Door'])

        # Adding model 'Status'
        db.create_table(u'garage_app_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('door', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['garage_app.Door'])),
            ('distance', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=4)),
            ('isDoorUp', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('isCarPresent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isError', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('statusDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('garage_app', ['Status'])


    def backwards(self, orm):
        # Deleting model 'Relay'
        db.delete_table(u'garage_app_relay')

        # Deleting model 'Sensor'
        db.delete_table(u'garage_app_sensor')

        # Deleting model 'Led'
        db.delete_table(u'garage_app_led')

        # Deleting model 'RgbLed'
        db.delete_table(u'garage_app_rgbled')

        # Deleting model 'Door'
        db.delete_table(u'garage_app_door')

        # Deleting model 'Status'
        db.delete_table(u'garage_app_status')


    models = {
        'garage_app.door': {
            'Meta': {'object_name': 'Door'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'relay': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['garage_app.Relay']"}),
            'rgbLed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['garage_app.RgbLed']"}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['garage_app.Sensor']"})
        },
        'garage_app.led': {
            'Meta': {'object_name': 'Led'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pin': ('django.db.models.fields.IntegerField', [], {})
        },
        'garage_app.relay': {
            'Meta': {'object_name': 'Relay'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relayPin': ('django.db.models.fields.IntegerField', [], {})
        },
        'garage_app.rgbled': {
            'Meta': {'object_name': 'RgbLed'},
            'blueLed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blueLed'", 'to': "orm['garage_app.Led']"}),
            'greenLed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'greenLed'", 'to': "orm['garage_app.Led']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redLed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'redLed'", 'to': "orm['garage_app.Led']"})
        },
        'garage_app.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'echoPin': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'triggerPin': ('django.db.models.fields.IntegerField', [], {})
        },
        'garage_app.status': {
            'Meta': {'object_name': 'Status'},
            'distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '4'}),
            'door': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['garage_app.Door']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isCarPresent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isDoorUp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'isError': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'statusDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['garage_app']