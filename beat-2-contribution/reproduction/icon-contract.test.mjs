// Reproduction evidence for betterlaspinas/betterlaspinas#274, not a fix.
// Run against an unmodified checkout: ICON_REPRO_REPO=/path/to/checkout node --test icon-contract.test.mjs
import { readFileSync } from 'node:fs'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
import assert from 'node:assert/strict'
import test from 'node:test'

const repo = process.env.ICON_REPRO_REPO
if (!repo) throw new Error('Set ICON_REPRO_REPO to the unmodified Better Las Piñas checkout')
const { validateAgainstSchema } = await import(pathToFileURL(path.join(repo, 'scripts/validate-config.mjs')).href)
const read = relative => JSON.parse(readFileSync(path.join(repo, relative), 'utf8'))
const schema = read('app/config/schema/services.schema.json')
const catalog = read('app/config/services.json')
const fixture = () => ({ id: 'icon-regression', title: 'Example Service', description: 'Test fixture only', categoryId: 'business', keywords: [], url: '/services/business', icon: 'bi-shop' })

test('positive control: a service with an icon is accepted by the real validator', () => {
  assert.equal(validateAgainstSchema({ services: [fixture()] }, schema, 'services'), true)
})
test('every current service has a nonblank icon', () => {
  const missing = catalog.services.filter(service => typeof service.icon !== 'string' || !service.icon.trim()).map(service => service.id)
  assert.deepEqual(missing, [], `Services lacking icons: ${missing.join(', ')}`)
})
test('the real validator rejects a service with no icon property', () => {
  const service = fixture()
  delete service.icon
  assert.equal(validateAgainstSchema({ services: [service] }, schema, 'services'), false)
})
test('the real validator rejects an empty icon value', () => {
  assert.equal(validateAgainstSchema({ services: [{ ...fixture(), icon: '' }] }, schema, 'services'), false)
})
